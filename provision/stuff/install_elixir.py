#!/usr/bin/env python3
from chibi.config import basic_config
from chibi_command.git import Git
from chibi_command.echo import cowsay
from chibi.file.snippets import cd
from chibi.file import Chibi_path


basic_config()
file_check_path = Chibi_path( '~/provision_installed' )
file_check = file_check_path.open()


version_to_check = "elixir\n".format( file=__file__, )


if __name__ == "__main__" and not version_to_check in file_check:
    cowsay( "instalando elixir" )

    Git.clone(
        "https://github.com/elixir-lang/elixir.git", dest='/tmp/elixir' )
    cd( '/tmp/elixir' )
