def concatenate(*args,**kwargs):
    result = "".join(args)
    for key, value in kwargs.items():
        result = result.replace(key, value) #prezapisvame kato vzimame keyq koito e duma i prosto slagame druga duma koqto e valueto na tozi key
    return result

