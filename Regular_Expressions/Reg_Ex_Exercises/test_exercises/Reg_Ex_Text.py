##############################################
########### WORKING WITH REGEX ###############
##############################################

import re           # importing library to work with RegEx

# target text
text_to_be_searched = """Hey Mr. Bezos,
                        I hope its okay I message you in this unsecure email program. Sry about that!
                        Here the list of extremely confidential clients and close coworkers of you who actually visited Epsteins island. 
                        Oh boy how I hope no random Python Students extract this sensitive list with some kind of regular expressions!
                        therealjeffbezos@bossnet.com
                        markzuckerbergtheman@facebookormetaidkmail.com
                        donaldtothatrump@getthatcapitolmail.com
                        2pacaintdeadandnowchillinonwrongislands@mail.com
                        Let me give you for some reason also your most important passwords to continue running amazon! 
                        Sorry Im new at this job.
                        epsteindidntkillhimself14141
                        ThIs1s4ctua11YaG00dPa$$w0rD
                        123456seven
                        password
                        Kind regards,
                        the soon to be fired secretary Tanisha
                        """

pattern = "\w+@\w+.\w+"                             # [\w] search for all any letter, digit or underscore. Equivalent to [a-zA-Z0-9_]
                                                    # [+] search for one or more repetions of any letter, digit or underscore
                                                    # [.\w] after a dot[.] - it search for all any letter, digit or underscore, Equivalent to [a-zA-Z0-9_] 

x = re.findall(pattern, text_to_be_searched)        # creating variable with method to find all items matching the pattern in the target text

print(x)                                            # print list of emails 