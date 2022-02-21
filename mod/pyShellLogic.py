while True:
    pyshellCommand=input('pyshell$ ')
    if pyshellCommand=='exit':
        break
    elif pyshellCommand=='run':
        appName=input('Please enter App Name:')
        import appLib
        appLoaderObject=appLib.AppLoader()
        appLoaderObject.loadAppByName(appName)
        del appName
    elif pyshellCommand=='appManaage':
        appName=input('Please enter App Name:')
        appManaageOpthion=input('What do you want to do?\nUnRegister\nRegister\nGetAppList\n')
        if appManaageOpthion=='UnRegister':
            import appManaage
            appUnRegisterObject=appManaage.AppManaage()
            appUnRegisterObject.appUnRegister(appName)
            del appUnRegisterObject
        elif appManaageOpthion=='Register':
            appPath=input('Please enter App Path:')
            import appManaage
            appRegisterObject=appManaage.AppManaage()
            appRegisterObject.appRegister(appName,appPath)
            del appRegisterObject
        elif appManaageOpthion=='GetAppList':
            import appManaage
            getAppListObject=appManaage.AppManaage()
            getAppListObject.getAppList()
        del appName
        del appManaageOpthion
    else:
        exec(pyshellCommand)