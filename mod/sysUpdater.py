class SysUpdater(object):
    def __init__(self):
        pass
    def sysCheckUpdate(self,ver):
        import requests
        ver=requests.get('http://hinayand.github.io/hinayand-project-info/hinayand-project-version.txt').text()
        if int(ver)>ver:
            return True
        else:
            return False
    def sysUpdate(self):
        updateScript=requests.get('http://hinayand.github.io/hinayand-project-info/hinayand-project-update-script.sh').text
        updateScriptIO=open('hinayand-project-update-script.sh','w')
        updateScriptIO.write(updateScript)
        print('System has a new version.\nIf you want to update,you can run the "hinayand-project-update-script.sh" to update!')