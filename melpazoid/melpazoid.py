_RETURN_CODE = 0  # eventual return code when run as script
_PKG_SUBDIR = 'pkg'  # name of directory for package's files
def _run_checks(
    subprocess.check_output(['rm', '-rf', _PKG_SUBDIR])
    os.makedirs(_PKG_SUBDIR)
        target = os.path.join(_PKG_SUBDIR, target)
        os.makedirs(os.path.join(_PKG_SUBDIR, os.path.dirname(file)), exist_ok=True)
    print()
    >>> _main_file(['pkg/a.el', 'pkg/b.el'], '(a :files ...)')
    'pkg/a.el'
        # NOTE: emacs --script <file.el> will set `load-file-name' to <file.el>
        # which can disrupt the compilation of packages that use that variable:
    _note('### Packaging ###\n', CLR_INFO)
    _check_recipe(files, recipe)
    _check_license(files, elisp_dir, clone_address)
    print()
    _note('<!-- ### Footnotes ###', CLR_INFO, highlight='### Footnotes ###')
    print('-->\n')
def _check_recipe(files: List[str], recipe: str):
    _note('### Similarly named ###\n', CLR_INFO)
    print()
            _run_checks(recipe, elisp_dir)
            _run_checks(recipe, elisp_dir, clone_address)
            _run_checks(recipe, elisp_dir, clone_address, pr_data)