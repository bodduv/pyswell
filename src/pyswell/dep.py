# -*- coding: utf-8 -*-

"""Infrastructure to manage locating or building project dependencies."""

import llnl.util.tty as tty
import os
import shutil
import spack.cmd
import spack.config
import spack.repo
import sys
from pathlib import Path
from spack.stage import DIYStage


def import_spack():
    """Locate spack library and import files.

    The code in this function is in part taken from
    spack/bin/spack bilingual file and modified according to need.
    """
    spack_path = Path(shutil.which('spack')).resolve()
    spack_prefix = spack_path.parent.parent
    spack_lib_path = spack_prefix / 'lib' / 'spack'
    spack_external_libs = spack_lib_path / 'external'

    sys.path.insert(0, str(spack_lib_path))
    sys.path.insert(0, str(spack_external_libs))
    print(sys.path)

    import spack.main
    from spack.spec import Spec
    s = Spec('dealii').concretized()
    print(s.architecture)
    import spack.store
    gcc_query_spec = Spec('%gcc')
    gcc_specs = spack.store.db.query(gcc_query_spec)
    import spack.cmd
    spack.cmd.parse_specs(gcc_specs)


def build(self, args):
    if not args.spec:
        tty.die("spack dev-build requires a package spec argument.")

    specs = spack.cmd.parse_specs(args.spec)
    if len(specs) > 1:
        tty.die("spack dev-build only takes one spec.")

    spec = specs[0]
    if not spack.repo.path.exists(spec.name):
        tty.die("No package for '{0}' was found.".format(spec.name),
                "  Use `spack create` to create a new package")

    if not spec.versions.concrete:
        tty.die(
            "spack dev-build spec must have a single, concrete version. "
            "Did you forget a package version number?")

    spec.concretize()
    package = spack.repo.get(spec)

    if package.installed:
        tty.error("Already installed in %s" % package.prefix)
        tty.msg("Uninstall or try adding a version suffix for this dev build.")
        sys.exit(1)

    source_path = args.source_path
    if source_path is None:
        source_path = os.getcwd()
    source_path = os.path.abspath(source_path)

    # Forces the build to run out of the current directory.
    package.stage = DIYStage(source_path)

    # disable checksumming if requested
    if args.no_checksum:
        spack.config.set('config:checksum', False, scope='command_line')

    package.do_install(
        make_jobs=args.jobs,
        keep_prefix=args.keep_prefix,
        install_deps=not args.ignore_deps,
        verbose=not args.quiet,
        keep_stage=True,   # don't remove source dir for dev build.
        dirty=args.dirty,
        stop_before=args.before,
        stop_at=args.until)

    # drop into the build environment of the package?
    if args.shell is not None:
        spack.build_environment.setup_package(package, dirty=False)
        os.execvp(args.shell, [args.shell])


if __name__ == "__main__":
    build()
