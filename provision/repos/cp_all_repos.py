#!/usr/bin/env python3
import os

from chibi.config import basic_config
from chibi_command.echo import cowsay
from chibi.file import Chibi_path


basic_config()
provision_folder = Chibi_path( os.environ[ 'PROVISION_PATH' ] )

directory_of_repos = provision_folder + 'repos/*.repo'
destiny_of_repos = Chibi_path( '/etc/yum.repos.d' )

cowsay( "starting to copy repos" )
directory_of_repos.copy( destiny_of_repos, verbose=True )

origin_ls = set( a.base_name for a in directory_of_repos.ls() )
dest_ls = set( a.base_name for a in destiny_of_repos.ls() )

print( directory_of_repos )
print( origin_ls )
print( dest_ls )

if origin_ls.intersection( dest_ls ) != origin_ls:
    raise Exception(
        f"no se encontraron todos los repos en el destino"
        f"{origin_ls.intersection( dest_ls )}" )

cp_stable = destiny_of_repos + 'cp_stable.repo '
cp_stable.move( destiny_of_repos + 'cp:stable.repo' )

cowsay( "ending to copy repos" )
