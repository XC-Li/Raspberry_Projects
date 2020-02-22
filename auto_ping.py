# This is the program to run ping test on local network
# XC.Li @ Apr.10 2018


# read in ping_list and ping_config
def start_up(ping_list_fn, ping_config_fn):
    ping_list_file_name = ping_list_fn
    ping_list_file = open(ping_list_file_name,"r")
    ping_list = {}
    for line in ping_list_file:
        line = line.rstrip() # remove the \n on the end of each line
        name = line.split(":")[0]
        ip = line.split(":")[1]
        ping_list[name] = ip
    ping_list_file.close()

    ping_config_file_name = ping_config_fn
    ping_config_file = open(ping_config_file_name,"r")
    ping_config = {}
    for line in ping_config_file:
        line = line.rstrip()
        config_name = line.split(":")[0]
        config_value = line.split(":")[1]
        ping_config[config_name] = config_value
    ping_config_file.close()

    return ping_list, ping_config


ping_list, ping_config = start_up("ping_list.txt", "ping_config.txt")
print(ping_list)
print(ping_config)

