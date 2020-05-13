with open('Files/index.html','r') as webpage:
    with open('Files/output.txt','a') as wf:
        page=webpage.read()
        link_exit=True
        

        while link_exit:
            pos=page.find('<a href=')
            if pos ==-1:
                link_exit=False
            else:
                first_qoute=page.find('\"',pos)
                second_qoute=page.find('\"',first_qoute+1)
                url=page[first_qoute+1:second_qoute]
                print(url)
                
                wf.write(url +'\n')
                page=page[second_qoute:]
                print(page)
                
                
