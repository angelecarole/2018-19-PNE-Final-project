import http.server
import socketserver
import http.client
import json

PORT = 8000

socketserver.TCPServer.allow_reuse_address = True

class Testhandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        print(self.path)

        element_list = self.path.split('?')
        print(element_list)
        resource= element_list[0]
        if resource == '/':
            form = open('form.html','r')
            contents = form.read()
        elif resource == '/listSpecies':
            if len(element_list) == 1:
                HOSTNAME = "rest.ensembl.org"
                endpoint = "/info/species?content-type=application/json"
                method = "GET"
                headers = {'User-Agent':'http-client'}
                conn = http.client.HTTPSConnection(HOSTNAME)

                conn.request(method, endpoint, None, headers)

                # -- Read the response message from the server
                r1 = conn.getresponse()

                # -- Print the status line
                print("Response received!: {} {}\n".format(r1.status, r1.reason))

                # -- Read the response's body
                text = r1.read().decode("utf-8")
                # -- Create a variable with the data,
                # -- form the JSON received
                Species = json.loads(text)
                list_species = ''
                for i in Species['species']:
                    species = i['name']
                    print(species)
                    list_species = list_species +'<li>{}</li>'.format(species)
                    contents = """<!DOCTYPE html>
                                             <html lang="en">
                                               <head>
                                                 <meta charset="utf-8">
                                                 <title>List Species</title>
                                               </head>
                                                 <h1>List of species</h1>
                                                 <l>{}</l>
                                                 <br><br>
                                                 <a href="/">HOME PAGE</a>
                                               </body>
                                             </html>""".format(list_species)
            elif len(element_list)> 1:
                limit = element_list[1]
                optional = limit.split('=')
                optional1 = optional[1]
                print(optional1)
                HOSTNAME = "rest.ensembl.org"
                endpoint = "/info/species?content-type=application/json"
                method = "GET"
                headers = {'User-Agent': 'http-client'}
                conn = http.client.HTTPSConnection(HOSTNAME)

                conn.request(method, endpoint, None, headers)

                # -- Read the response message from the server
                r1 = conn.getresponse()

                # -- Print the status line
                print("Response received!: {} {}\n".format(r1.status, r1.reason))

                # -- Read the response's body
                text = r1.read().decode("utf-8")
                # -- Create a variable with the data,
                # -- form the JSON received
                Species = json.loads(text)
                number = 0
                list_species = ''
                for i in Species['species']:
                    number+= 1
                    if number <= int(optional1):
                        species = i['name']
                        print(species)


                        list_species = list_species + '<li>{}</li>'.format(species)
                        contents = """<!DOCTYPE html>
                                                                 <html lang="en">
                                                                   <head>
                                                                     <meta charset="utf-8">
                                                                     <title>List Species</title>
                                                                   </head>
                                                                     <h1>List of species</h1>
                                                                     <l>{}</l>
                                                                     <br><br>
                                                                     <a href="/">HOME PAGE</a>
                                                                   </body>
                                                                 </html>""".format(list_species)




        elif resource == '/karyotype':

            HOSTNAME = "rest.ensembl.org"
            endpoint1 = "/info/assembly/"
            endpoint2 = "?content-type=application/json"
            print(self.path)
            answer = self.path.split('?')
            print(answer)
            choices = answer[1]
            print(choices)
            input = choices.split('=')
            species = input[1]
            print(species)
            method = "GET"
            headers = {'User-Agent': 'http-client'}

            conn = http.client.HTTPSConnection(HOSTNAME)

            """input = choices.split('=')
            species = input[1]
            print(species)"""

            conn.request(method, endpoint1 + species + endpoint2, None, headers)

            # -- Read the response message from the server
            r2 = conn.getresponse()

            # -- Print the status line
            print("Response received!: {} {}\n".format(r2.status, r2.reason))

            # -- Read the response's body
            text = r2.read().decode("utf-8")
            # -- Create a variable with the data,
            # -- form the JSON received
            karyotype = json.loads(text)
            the_karyotype = ''
            for i in karyotype['karyotype']:
                choices = i
                print(choices)
                the_karyotype = the_karyotype + '<li>{}</li>'.format(choices)
                contents = """<!DOCTYPE html>
                                             <html lang="en">
                                               <head>
                                                 <meta charset="utf-8">
                                                 <title>the karyotype</title>
                                               </head>
                                                 <h1> karyotype</h1>
                                                 <l>{}</l>
                                                 <br><br>
                                                 <a href="/">HOME PAGE</a>
                                               </body>
                                             </html>""".format(the_karyotype)

        elif resource == '/chromosomeLength':

            HOSTNAME = "rest.ensembl.org"
            endpoint1 = "/info/assembly/"
            endpoint2 = "?content-type=application/json"
            print(self.path)
            answer = self.path.split('?')
            print(answer)
            choices = answer[1]
            print(choices)
            input = choices.split('=')
            species = input[1]
            print(species)
            chromosome = input[2]
            animal = species.split('&')
            animals = animal[0]
            print(animals)
            method = "GET"
            headers = {'User-Agent': 'http-client'}


            conn = http.client.HTTPSConnection(HOSTNAME)

            """input = choices.split('=')
            species = input[1]
            print(species)"""

            conn.request(method, endpoint1 + animals + endpoint2, None, headers)

            # -- Read the response message from the server
            r2 = conn.getresponse()

            # -- Print the status line
            print("Response received!: {} {}\n".format(r2.status, r2.reason))

            # -- Read the response's body
            text = r2.read().decode("utf-8")
            # -- Create a variable with the data,
            # -- form the JSON received
            chromosomes = json.loads(text)
            the_chromosome = ''
            for i in chromosomes['top_level_region']:
                name = i['name']
                if (name == chromosome ) and (i['coord_system']=='chromosome'):
                    length = i['length']
                    contents = """<!DOCTYPE html>
                                                         <html lang="en">
                                                           <head>
                                                             <meta charset="utf-8">
                                                             <title>the chromosome</title>
                                                           </head>
                                                             <h1> chromosome</h1>
                                                             <l>{}</l>
                                                             <br><br>
                                                             <a href="/">HOME PAGE</a>
                                                           </body>
                                                         </html>""".format(length)









            # Generating the response message
        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(str.encode(contents))


# -- Open the socket server
with socketserver.TCPServer(("", PORT), Testhandler) as httpd:


    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()

print("")
print("Server Stopped")