import requests

numberOfInstances = input("Please enter a max instance number: ex. 06\n")

TotalProjects = 0

for i in range(0, numberOfInstances):
    #Authenticate
    r1 = requests.post("https://tc" + "%.2d" % i + ".blackducksoftware.com:443/j_spring_security_check", data={'j_username': 'test', 'j_password': 'test'})
    #Store cookies
    cookies = dict(JSESSIONID=r1.cookies['JSESSIONID'])
    #Get Projects
    r2 = requests.get("https://tc" + "%.2d" % i + ".blackducksoftware.com:443/api/projects", data={'j_username': 'test', 'j_password': 'test'}, cookies=cookies)
    print r2.json()["totalCount"]
    TotalProjects += r2.json()["totalCount"]

print "Total Projects for all Instances: ", TotalProjects
