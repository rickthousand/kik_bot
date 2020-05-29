import time
import uuid
import requests
from kik_unofficial.utilities.cryptographic_utilities import CryptographicUtils
import kik_unofficial.datatypes.xmpp.chatting as chatting
from kik_unofficial.client import KikClient
from kik_unofficial.callbacks import KikClientCallback
from kik_unofficial.datatypes.xmpp.errors import SignUpError, LoginError
from kik_unofficial.datatypes.xmpp.roster import FetchRosterResponse, PeersInfoResponse
from kik_unofficial.datatypes.xmpp.sign_up import RegisterResponse, UsernameUniquenessResponse
from kik_unofficial.datatypes.xmpp.login import LoginResponse, ConnectionFailedResponse

username = 'thefuckbot0'
password = 'Callofdutymw1'

group_members={}

def main():
    bot = EchoBot()


def listToString(self, s):
    str1 = ''
    return (str1+' \n\n'.join(s))


class EchoBot(KikClientCallback):
    def __init__(self):
        self.client = KikClient(self, username, password)
    def on_authenticated(self):
        print("Now I'm Authenticated, let's request roster")
        self.client.request_roster()
    def on_login_ended(self, response: LoginResponse):
        print("Full name: {} {}".format(response.first_name, response.last_name))

    def on_chat_message_received(self, chat_message: chatting.IncomingChatMessage):
        print("[+] '{}' says: {}".format(chat_message.from_jid, chat_message.body))
        print("[+] Replaying.")
        self.client.send_chat_message(chat_message.from_jid, "You said \"" + chat_message.body + "\"!")

    def on_message_delivered(self, response: chatting.IncomingMessageDeliveredEvent):
        print("[+] Chat message with ID {} is delivered.".format(response.message_id))

    def on_message_read(self, response: chatting.IncomingMessageReadEvent):
        print("[+] Human has read the message with ID {}.".format(response.message_id))



    def on_group_message_received(self, chat_message: chatting.IncomingGroupChatMessage):
        if chat_message.body.lower()=='a':
            self.client.send_chat_message(chat_message.group_jid, str(group_members[chat_message.group_jid]))
        if chat_message.body.lower()=="my jid":
            self.client.send_chat_message(chat_message.group_jid, chat_message.from_jid)
        if chat_message.body.lower()=='!2000':
            self.client.send_custom_stanza('<message type="groupchat" to="1100244974579_g@groups.kik.com" id="[UUID]" ><kik qos="true" app="all"/><request d="true" xmlns="kik:message:receipt" r="true"><g jid="1100244974579_g@groups.kik.com"><m s="1" a="1">shutupisay743_fm1@talk.kik.com</m></g><status jid="shutupisay743_fm1@talk.kik.com"> Name has been promoted to owner</sysmsg></request></message>')
        if chat_message.body.lower()=='!ping':
            self.client.send_chat_message(chat_message.group_jid, "vilppu is a scammer")

        if chat_message.body.lower().startswith("!echo"):
            a=chat_message.body.lower()
            b=a.split('!echo', maxsplit=1)
            query=b[1] and b[1]
            self.client.send_chat_message(chat_message.group_jid, query)


        q=chat_message.body.lower()
        if '==' in q:
            f,l=q.split('==', maxsplit=1)
            self.client.send_chat_message(chat_message.group_jid, f'you say {f}, i say{l}')

        if 'nigger' in chat_message.body.lower():
            self.client.remove_peer_from_group(chat_message.group_jid, chat_message.from_jid)
            self.client.send_chat_message(chat_message.group_jid, 'Removing the racist...')

        if chat_message.body.lower().startswith("!news"):
            a=chat_message.body.lower()
            b=a.split()
            query=b[1] and b[1]
            self.client.send_chat_message(chat_message.group_jid, 'Query : '+query)
            main_url = f"https://newsapi.org/v2/everything?q={query}&apiKey=4dbc17e007ab436fb66416009dfb59a8"
            open_bbc_page = requests.get(main_url).json()
            article = open_bbc_page["articles"]
            results = []
            a=''
            send=a.join(results[i] for i in range(len(results)))

            for ar in article:
                results.append(ar["title"])
            a=listToString(self, results)
            self.client.send_chat_message(chat_message.group_jid, a)

            #self.client.send_chat_message(chat_message.group_jid, listToString(results))

        if chat_message.body.lower() == "rick":
            self.client.send_chat_message(chat_message.group_jid, 'is cool')
        if chat_message.body.lower() == "ping":
                self.client.send_chat_message(chat_message.group_jid, "fuck vilppu")
        if chat_message.body.lower().startswith("!rm"):
            r = chat_message.body
            t = r.split()
            #inf = self.client.xiphias_get_users_by_alias('@anythingatallman')
            jid = self.client.get_jid(f'{t[1]}')
            self.client.remove_peer_from_group(chat_message.group_jid, jid)
            self.client.send_chat_message(chat_message.group_jid, jid)
        if chat_message.body.lower().startswith("!pm"):
            r = chat_message.body
            t = r.split()
            # inf = self.client.xiphias_get_users_by_alias('@anythingatallman')
            a_jid = self.client.get(f'{t[1]}')
            if group_members[chat_message.group_jid][jid]['is_owner']:

                    self.client.send_chat_message(chat_message.group_jid, 'is admin')
            self.client.promote_to_admin(chat_message.group_jid, jid)
            self.client.send_chat_message(chat_message.group_jid,'Promoted : '+ jid)
        if chat_message.body.lower().startswith("!ban"):
            r = chat_message.body
            t = r.split()
            # inf = self.client.xiphias_get_users_by_alias('@anythingatallman')
            jid = self.client.get_jid(f'{t[1]}')
            self.client.ban_member_from_group(chat_message.group_jid, jid)





        if chat_message.body.lower()=='!about':
            self.client.send_chat_message(chat_message.group_jid, "made by @smithyion")

        if chat_message.body.lower().startswith("!info"):
            r = chat_message.body
            t = r.split()
            a=self.client.get_jid(t[1])
            b=self.client.xiphias_get_users_by_alias(a)

            #inf = self.client.xiphias_get_users_by_alias(f'{t}')
            for i in range(len(b)):
                self.client.send_chat_message(chat_message.group_jid, b[i])
        if chat_message.body.lower()=='dee':
            self.client.send_chat_message(chat_message.group_jid, "Is legend")

        if chat_message.body.lower()=='vilppu':
            self.client.send_chat_message(chat_message.group_jid, "is a faggot")

        if chat_message.body.lower().startswith("!leave"):
            self.client.send_chat_message(chat_message.group_jid, "Leaving...")
            self.client.leave_group(chat_message.group_jid)

        if chat_message.body.lower().startswith("!unban"):
            r = chat_message.body
            t = r.split()
            # inf = self.client.xiphias_get_users_by_alias('@anythingatallman')
            jid = self.client.get_jid(f'{t[1]}')
            self.client.unban_member_from_group(chat_message.group_jid, jid)
            self.client.send_chat_message(chat_message.group_jid,'Banned : '+ jid)
        if chat_message.body.lower().startswith("!dm"):
            r = chat_message.body
            t = r.split()
            # inf = self.client.xiphias_get_users_by_alias('@anythingatallman')
            jid = self.client.get_jid(f'{t[1]}')
            self.client.send_chat_message(chat_message.group_jid, "Demoted : "+jid)
            self.client.demote_admin(chat_message.group_jid, jid)
        if chat_message.body.lower().startswith("!add"):
            r = chat_message.body
            t = r.split()
            # inf = self.client.xiphias_get_users_by_alias('@anythingatallman')
            jid = self.client.get_jid(f'{t[1]}')
            self.client.send_chat_message(chat_message.group_jid, "Adding : "+jid)
            self.client.add_peer_to_group(chat_message.group_jid, jid)
    '''	print("[+] '{}' from group ID {} says: {}".format(chat_message.from_jid, chat_message.body))'''

    def on_is_typing_event_received(self, response: chatting.IncomingIsTypingEvent):
        print("[+] {} is now {}typing.".format(response.from_jid, "not " if not response.is_typing else ""))

    def on_group_is_typing_event_received(self, response: chatting.IncomingGroupIsTypingEvent):
        print("[+] {} is now {}typing in group {}".format(response.from_jid, "not " if not response.is_typing else "",
                                                          response.group_jid))

    def on_roster_received(self, response: FetchRosterResponse):
            for peer in response.peers:
                if hasattr(peer, 'members'):
                    group_members[peer.jid]={}
                    for member in peer.members:
                        group_members[peer.jid][member.jid] = dict(is_admin=member.is_admin, is_owner=member.is_owner)


    def on_friend_attribution(self, response: chatting.IncomingFriendAttribution):
        print("[+] Friend attribution request from " + response.referrer_jid)

    def on_image_received(self, image_message: chatting.IncomingImageMessage):
        print("[+] Image message was received from {}".format(image_message.from_jid))
    
    def on_peer_info_received(self, response: PeersInfoResponse):
        print("[+] Peer info: " + str(response.users))

    def on_group_status_received(self, response: chatting.IncomingGroupStatus):
        print("[+] Status message in {}: {}".format(response.group_jid, response.status))

    def on_group_receipts_received(self, response: chatting.IncomingGroupReceiptsEvent):
        print("[+] Received receipts in group {}: {}".format(response.group_jid, ",".join(response.receipt_ids)))

    def on_status_message_received(self, response: chatting.IncomingStatusResponse):
        print("[+] Status message from {}: {}".format(response.from_jid, response.status))

    def on_username_uniqueness_received(self, response: UsernameUniquenessResponse):
        print("Is {} a unique username? {}".format(response.username, response.unique))

    def on_sign_up_ended(self, response: RegisterResponse):
        print("[+] Registered as " + response.kik_node)

    # Error handling

    def on_connection_failed(self, response: ConnectionFailedResponse):
        print("[-] Connection failed: " + response.message)

    def on_login_error(self, login_error: LoginError):
        if login_error.is_captcha():
            login_error.solve_captcha_wizard(self.client)

    def on_register_error(self, response: SignUpError):
        print("[-] Register error: {}".format(response.message))


if __name__ == '__main__':
    main()