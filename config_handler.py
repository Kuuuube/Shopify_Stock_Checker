from configparser import ConfigParser
import time
import hashlib

def config_info(config_file):
    config = ConfigParser()
    config.read(config_file)
    return config

def backup_bad_config(config_file):
    try:
        with open(config_file,"rb") as hashfile:
            bytes = hashfile.read()
            hash_value = hashlib.md5(bytes).hexdigest();
        with open(config_file, 'r') as conf, open(config_file + ".bak" + hash_value, "w") as backup:
            for line in conf:
                backup.write(line)
                
    except Exception:
        pass

def default_config(config_file):
    backup_bad_config(config_file)
    
    defaults = ConfigParser()
    defaults["stock"] = {
        "stock_delay": "5",
        "batch_delay": "0",
        "request_fail_delay": "60",
    }

    defaults["webhook"] = {
        "url": "",
        "content": "In Stock!\\nName: {Name}, Title: {Title}, SKU: {SKU}\\nLink: {Link}",
    }
    
    with open(config_file, 'w') as conf:
        defaults.write(conf)

def read(config_file,section,name):
    function_success = False
    while function_success == False:
        try:
            config = config_info(config_file)
            return config.get(section,name)
            function_success == True
            
        except Exception as e:
            print(e)
            if config_file == "config.cfg":
                print("Config corrupted. Reverting to default.")
                default_config(config_file)
            time.sleep(1)

def write(config_file,section,name,value):
    function_success = False
    while function_success == False:
        try:
            config = config_info(config_file)
            config[section][name] = value
            with open(config_file, 'w') as conf:
                config.write(conf)
            function_success = True
            
        except Exception as e:
            print(e)
            if config_file == "config.cfg":
                print("Config corrupted. Reverting to default.")
                default_config(config_file)
            time.sleep(1)
