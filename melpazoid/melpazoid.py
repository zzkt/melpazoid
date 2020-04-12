import configparser
    check_containerized_build(files, recipe)
    print_related_packages(recipe)
def check_containerized_build(files: list, recipe: str):
    package_name = _package_name(recipe)
    main_file = os.path.basename(_main_file(files, recipe))
    output = subprocess.check_output(['make', 'test', f"PACKAGE_MAIN={main_file}"])
    """Use the GitHub API to check for a license."""
    _fail('- Use a LICENSE file that GitHub can detect (e.g. no markup) if possible')
                print(f"<!-- {license_} excerpt: `{stream.readline().strip()}...` -->")
        with open(file) as stream:
            license_ = _check_file_for_license_boilerplate(stream)
            _fail(
                '- Please add license boilerplate or an [SPDX license identifier]'
                '(https://spdx.org/using-spdx-license-identifier)'
                f" to {basename}"
            )
def _check_file_for_license_boilerplate(el_file: TextIO) -> str:
    """Check an elisp file for some license boilerplate.
    >>> _check_file_for_license_boilerplate(io.StringIO('SPDX-License-Identifier:  ISC '))
    'ISC'
    >>> _check_file_for_license_boilerplate(io.StringIO('GNU General Public License'))
    'GPL'
    """
    text = el_file.read()
    # SPDX license identifiers are easy https://spdx.org/using-spdx-license-identifier
    match = re.search('SPDX-License-Identifier:[ ]+(.*)', text, flags=re.I)
    if match:
        return match.groups()[0].strip()
    # otherwise, look for fingerprints (consider <https://github.com/emacscollective/elx>)
    fingerprints = [
        ('Unlicense', 'This is free and unencumbered software released into'),
        ('Apache 2.0', 'Licensed under the Apache License, Version 2.0'),
        ('BSD 3-Clause', 'Redistribution and use in source and binary forms'),
    for license_key, license_text in fingerprints:
        if re.search(license_text, text):
            print(
                f"- {CLR_ULINE}{file}{CLR_OFF}"
                f" ({_check_file_for_license_boilerplate(stream) or 'unknown license'})"
                + (f" -- {header}" if header else "")
            )
    package_name = _package_name(recipe)
    shorter_name = package_name[:-5] if package_name.endswith('-mode') else package_name
    known_packages = _known_packages()
    known_names = [name for name in known_packages if shorter_name in name]
    if not known_names:
        return
    _note('\n### Similarly named packages ###\n', CLR_INFO)
    for name in known_names[:10]:
        print(f"- {name} {known_packages[name]}")
    if package_name in known_packages:
        _fail(f"- {package_name} {known_packages[package_name]} is in direct conflict")
def _known_packages() -> dict:
    melpa_packages = {
        package: f"https://melpa.org/#/{package}"
    epkgs = 'https://raw.githubusercontent.com/emacsmirror/epkgs/master/.gitmodules'
    epkgs_parser = configparser.ConfigParser()
    epkgs_parser.read_string(requests.get(epkgs).text)
    epkgs_packages = {
        epkg.split('"')[1]: 'https://' + data['url'].replace(':', '/')[4:]
        for epkg, data in epkgs_parser.items()
        if epkg != 'DEFAULT'
    }
    return {**epkgs_packages, **melpa_packages}
        if _clone(clone_address, into=elisp_dir, branch=_branch(recipe), scm=scm):
def _clone(repo: str, into: str, branch: str = None, scm: str = 'git') -> bool:
    print(f"Checking out {repo}")
        _fail(f"Unable to locate {repo}")
    if scm == 'git':
        # MELPA recipe must specify the branch using the :branch keyword
        options = ['--branch', branch if branch else 'master']
        options += ['--depth', '1', '--single-branch']
        options = ['--branch', branch] if branch else []
    git_command = [scm, 'clone', *options, repo, into]
    if filename != _package_name(recipe):
        _fail(f"Filename '{filename}' does not match '{_package_name(recipe)}'")
        return
        if _clone(clone_address, into=elisp_dir, branch=_branch(recipe)):