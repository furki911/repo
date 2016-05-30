#!/usr/bin/env python3

from lilaclib import *

build_prefix = 'extra-x86_64'
post_build = aur_post_build

_pkg_name = 'google-chrome'

dotinstall = '''
note() {
    printf "${blue}==>${yellow} NOTE:${bold} $1${all_off}\n"
}

all_off="$(tput sgr0)"
bold="${all_off}$(tput bold)"
blue="${bold}$(tput setaf 4)"
yellow="${bold}$(tput setaf 3)"

post_install() {
    note "Custom flags should be put directly in: ~/.config/chrome-flags.conf"
    note "The launcher is called: 'google-chrome-stable'"
}

post_upgrade() {
    post_install
}
'''

def pre_build():
  aur_pre_build()
  with edit_file('%s.install' % _pkg_name) as f:
    print(dotinstall)


if __name__ == '__main__':
  single_main(build_prefix)
