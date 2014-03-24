import pycurl
 
c = pycurl.Curl()
c.setopt(c.URL, 'http://murmuring-crag-3099.herokuapp.com/')
c.setopt(c.POSTFIELDS, 'reading=890&user_id=008&plant_id=5')
c.perform()