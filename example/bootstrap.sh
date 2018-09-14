#!/bin/bash
# Copyright 2018 The MUSSLES Developers
#
# This file is part of MUSSLES.
#
# MUSSLES is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# MUSSLES is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with MUSSLES.  If not, see <http://www.gnu.org/licenses/>.

__bootstrap() {

  local VERSION='0.1.0'
  local UNRECOGNIZED_CMD=2

  ## Subcommands ##

  # bootstrap run
  run() {
    # Set up
    \mkdir -p output
    \mkdir -p output/h750a
    \mkdir -p output/h750a/plots
    \mkdir -p output/h750a/parameters
    \mkdir -p output/h765a
    \mkdir -p output/h765a/plots
    \mkdir -p output/h765a/parameters
    # Run the pipeline
    \sspipeline --config configs/config_h750a.json
    \sspipeline --config configs/config_h765a.json
  }

  # bootstrap test
  test() {
    # Set up
    \mkdir -p output
    \mkdir -p output/plots
    \mkdir -p output/parameters
    # Test the pipeline
    \sspipeline --config configs/test_config.json
  }

  # bootstrap help
  print_usage() {
    echo 'Usage:
  bootstrap.sh --version    # display the version number and exit
  bootstrap.sh --help       # display this text and exit
  bootstrap.sh run          # run the examples
  bootstrap.sh test         # test the example (used by Travis CI)'
    echo
    echo 'What This Will Do:
  TODO'
  }

  # bootstrap version
  print_version() {
    echo "bootstrap.sh v$VERSION"
  }

  ## /commands ##

  if [ $# -eq 0 ]; then
    print_usage
    return 0
  fi

  case "$1" in

    -v|--version|version)
      print_version
      return 0;;

    -h|--help|-help|help)
      print_usage
      return 0;;

    -*)
      echo "Unrecognized option: $1"
      print_usage
      return $UNRECOGNIZED_CMD;;

    run)
      shift;
      run "$@"
      return $?;;

    test)
      shift;
      test "$@"
      return $?;;

    _*)
      print_usage
      return 1;;

  esac

}

__bootstrap "$@"
