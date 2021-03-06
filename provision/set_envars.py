#!/usr/bin/env python3
import sys
from chibi.config import basic_config
from chibi_command.echo import cowsay
from chibi.file import Chibi_path


basic_config()

if __name__ == "__main__":
    path = sys.argv[1]
    profile = Chibi_path( '/etc/profile.d/' )
    provision = profile + 'provision.sh'
    provision.open().write( f'export PROVISION_PATH={path}' )

    local_bin = profile + 'local_bin.sh'
    local_bin.open().write( f'export PATH="$PATH:/usr/local/bin"' )
