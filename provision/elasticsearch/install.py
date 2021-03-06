#!/usr/bin/env python3
from chibi.config import basic_config
from chibi_command.echo import cowsay
from chibi.file import Chibi_path
from chibi_command.centos import Yum
from chibi_command.nix import Systemctl
from chibi_command.rpm import RPM


basic_config()
file_check_path = Chibi_path( '~/provision_installed' )
file_check = file_check_path.open()


version_to_check = "elasticsearch 6\n".format( file=__file__, )


if __name__ == "__main__" and not version_to_check in file_check:
    cowsay( "Starting install for elasticsearch" )

    RPM.rpm_import( 'https://artifacts.elastic.co/GPG-KEY-elasticsearch' )
    result = Yum.install( 'elasticsearch' )
    if not result:
        raise Exception(
            f"no se puedo instalar elasticsearch {vars(result)}" )

    Systemctl.daemon_reload().run()
    Systemctl.enable( 'elasticsearch.service' ).run()
    Systemctl.start( 'elasticsearch.service' ).run()

    #command(
    #    '/usr/share/elasticsearch/bin/plugin', 'install',
    #    'royrusso/elasticsearch-HQ' )

    file_check.append( version_to_check )
    cowsay( "Ending install for elasticsearch" )
