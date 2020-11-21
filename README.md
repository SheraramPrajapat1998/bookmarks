- Add 127.0.0.1:8000 in etc/environment file and name it mysite.com

- run https trusted server
  python manage.py runserver_plus --cert-file cert.crt

After running https server: go to https://mysite.com:8000/login/

then reigster/login then drag the BOOKMARK IT button to the bookmarks toolbar of your browser

Open a website of your own choice in your browser and click on your bookmarklet.
You will see that a new white box appears on the website, displaying all JPEG images found with dimensions higher than 100×100 pixels.
for e.g.: https://www.shutterstock.com/search/rajasthan


Select any image it will redirect to form where you can fill form and save that image.


#### NOTE:
- When you are accessing your site through HTTPS. Your browser might show a security
  warning because you are using a self-generated certificate. If this is the case, access
  the advanced information displayed by your browser and accept the self-signed
  certificate so that your browser trusts the certificate.
  
- You need to run redis server to view most viewed images and total views on an image. 
