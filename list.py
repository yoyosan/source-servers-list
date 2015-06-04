import sys
import os

from valve.source import master_server
from valve.source import a2s
from valve.source import messages

msq = master_server.MasterServerQuerier()
stop_address = u"0.0.0.0"
address = u"1.2.3.4"
no_servers = 0

while address != stop_address:
    try:
        print "\t---------- Number of servers:", no_servers
        for address in msq.find(region=[u"all"],
                                gamedir=u"csgo",
                                gametype=[u"idle", u"secure"]
                                ):
            try:
                server = a2s.ServerQuerier(address)
                info = server.get_info()
                players = server.get_players()

                print "Address: %s:%s" % (address[0], address[1]), " - {player_count}/{max_players} - {map}".format(
                    **info), info["server_name"], "\n"
                for player in sorted(players["players"],
                                     key=lambda p: p["score"], reverse=True):
                    print "\t", "{score}".format(**player), player["name"]

                no_servers += 1
            except messages.BrokenMessageError:
                continue

    except a2s.NoResponseError:
        print "Master server request timed out!"
        continue

print 'Number of servers', no_servers
