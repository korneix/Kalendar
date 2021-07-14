import discord as dc



# When the channel and the server ID are valid, this function saves and stores
# the channel in which the bot is supposed to send the birthday reminders.
# Raises a ValueError exception when the parameters don't meet the requirements
# listed below.
# Parameters :
#   - channel: Channel object. Must correspond to an existing Discord channel.
#   - server: Server object. Must correspond to an existing Discord server.
# Returns :
#   - True if the binding was successful, False otherwise.
#
def bindto(channel, server):
    return False


# Will browse the list of registered servers (i.e. servers in which the /bind
# command was used at least once) and returns their IDs. If the parameter does
# not meet the requirements listed below, does nothing.
# Parameters :
#   - user: User() object. Must point to a valid Discord user.
# Returns :
#   - The list of server IDs where the user is present. Otherwise, returns [].
def getuserservers(user):
    return []


# If the user and the date are both valid, saves and stores the user ID and its
# associated birthday. Otherwise, does nothing if the date doesn't meet the
# requirements listed below.
# Parameters :
#   - user: User object. Must correspond to an existing Discord user.
#   - day: Integer. 0 < day < 32
#   - month: Integer. 0 < month < 13
#   - year: Integer. year >= 1900
# Returns :
#   - True if the date was successfuly stored, False otherwise.
#
def setbirthday(user, day, month, year):
    return False


# Tries to fetch a user ID and its associated birthday from a valid date
# passed in parameters. If the date doesn't meet the requirements listed below,
# does nothing.
# Parameters :
#   - day: Integer. 0 < day < 32
#   - month: Integer. 0 < month < 13
#   - year: Integer. year <= 1950
# Returns :
#   - A corresponding Entry() object if a birthdate was found, None otherwise.
#
def getbybirthdate(day, month, year):
    return None


# Performs a similar action than the function above. However, this time, the
# research criteria is the ID of the user passed in parameters. Here as well,
# if the parameters doesn't meet the requirements listed below, does nothing.
# Parameters :
#   - user: User() discord object. Must point to a valid user.
# Returns :
#   - A corresponding Entry() object if a birthdate was found, None otherwise.
#
def getbyid(user):
    return None


# Verifies if there is any birthday set on the date passed in parameters. If the
# date is invalid, i.e. if it doesn't meet the requirements listed below, does
# nothing.
# Parameters:
#   - day: Integer. 0 < day < 32
#   - month: Integer. 0 < month < 13
# Returns :
#   - A list of Entry() objects if successful, an empty list otherwise.
#
def geteventsoftheday(day, month):
    return []
