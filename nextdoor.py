from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
import time

#set up your next-door account here:
UserEmail = ""
Password = ""

# define 

info_cat_dic = {"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAoCAMAAAC7IEhfAAABAlBMVEUAAABweoVxd4JvdoJwd4Fvd4FveIFvdoFxeIdwd4Jvd4Fwd4Fwd4FyeYaAgJVweINvd4Jwd4JxdoOqqqpvdoJwd4Jwd4H///9vd4NweoVvdoJveIJweIRxgI5wdoJxjo5wdoJ3d4hze4RyeYNwd4JxdoFweIFvd4FvdoKZmZlwd4JydoRwd4JveYJvd4JwdoFwdoFxeINwd4JyeYNwdoGAgJlwdoJveINweIN3d4hwd4Fxd4Jwd4Fvd4JvdoGAgL9wd4FxeINvd4F0eoVwdoJwd4KSkpJwdoJwd4Jwd4FvdoJveYNwd4J1fINxeIdvdoJvd4JwdoFzeYZwdoJwdoJxd4NP8fr4AAAAVnRSTlMAMoG+2fNV/yLI45RJJgxA7ORjA/qwkAFlGbyTWRL2CeIeH0y9iIZH3AXwOJ836uvLcXJK6QrGdUIPli39h9EE3Ub3LJnSB9iP+f5OdCMk2qWmKvJwb/HYmHMAAAGoSURBVHgBfJAFlsMwEMXCCjOXufe/4FLgxbCdoP+TQWNIZVq247qObZnGp/Ic1nK8fzE/gDCKkzRN4iiEwNdzWU5RVsuoKgvyTMvVNOk2SBtqDenntJ0YdS25untAs+UmsiFQfClSdZu0QHZ3KOdV+sB1g35evcSR+kw4+Q4jfzUOk3uI2HmL3bTeSLgfhn3IOK0ZYQmgTfz37QkPv99DSP8XxNjSEZPZfT8F+9k3kQ7pks7fYQoG3MkbVwCPnPTgiaMAnrnot75ylmRuepkbdwF88NS358lDAF+8DV3DjTcvAfxupB6sIwjDKAy/4W1gj6LVwdq2NTH6LyXmj8k8FXy82ZzyrhXmlcvyR0GnOJyqwF9FleJY4mUVMVRUxVJTBVNdjSaGZkN1LC21MbTVwtZRucsf3bI6OByoxx89HeDSjw3y/JIfxPo4DTUa82080hC3+OR3P21N4nhMNZvzaT7TFK+FliverZZa4Ndca8O7jdZNQuxtdwGvgt12j1CXyl3BdU6XmKxcGsXjIzuxLN0b3d7ppsu/7h+kh3siSA8GaSJ5fML2Av9jJ9h7zBUkAAAAAElFTkSuQmCC":"Addr",\
"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAoCAYAAACM/rhtAAAD1ElEQVR4AdVYA5QsSwz9tm3btm3btm2z0rs7SQ1On59UP2Nx8G3btm3bLzPV6x13v/N6vZOaun1TubnpySbJ67///ps8sLwboDxkkD/Qr8AKZW4YM+9EB2do2JKG+DGD/F//LyD5LMjJRhMNHKDsY1B+9GA+NCSHEbm5W0hWBZI79P/6egvx6qmDayE+Akj+LYIgGUM0apber7e3t08JJMNjJq2VBVIDF2R5k25w1p0zVFwYPj21QbnbM3m3ntVUCsIQv+yZu7pSvKZcGSwxyeemkFpZtbgZyscT0jhNVYxbt22JcfkjsNFyyabX8gkl9pzUVO0oBc/6vcnKCvJZRQatg1rWaREZ5M91bUuWt0xOWqwc6StzRN03RzI+8TNoUN6rdW1bIVrMp/mTJKt4ChVl3Ujlpib2s7J+qcD406Q7yBW+kjurXaNCDcRveLnJJ1souWg+QPm5uFnWrVspXqXFEH/kz98rYdg+a/J92PJVuqEaBU17ecb5ac/4A63cPkcq7U5EZu5mBeWMCgC/KUkTX5OqYQisbO+r8re23Ijlh4yjaA+D/Je/mStS9oNOfKpfhhEjZhwapNsrBhmQuyQ1gGF40wy9zMOoshpq3b5A8nfJBcl5qYHU9ALxT75KTytfXO4gg/xPiUk5M71UW97be8R/WrJup7IgyZ0U+0lVg/SKhvgiL8Q/aUssG4t8cHwmDUrYX6pUjoo3gsLqhPQME906bcMg1UTE/VZ7b/lY3hFQfo27UgwAKNpZ22H/IUzfU+2ejhN1A9RNgOQez+Qb6qjLxevUByjfabyuA3LX9QJ1J5AcrWNFLPa+l79gctFqDYq4POPf7Gn9u1x8q41W7sfYX4F1p/cLKzFL/LY/Fn9okdU950BhxDxA/JZP3+OVWhyGIxbR6RCQR6vrGSouiqLpAivUXWTII+tOuZ5BIH43NgmtheELNs2XZqMdes3kHXUz2RaOnB9QXopNbjOHpgCHren7vNffOq98fvTsQPKoT/d3YN0WzfQDmm71A9ns8DkbaolA3OWr+0+tziYOcrd4Fo9ueOjvIyPkpLW9ffomaO/ZTXVKhuQQQ/yLv+vnA3IrNDiCdBZ7u+VTm+fIC7ySQXndp/x3QHe+ykX9DxL4e38Gm3flcu0zaR/uSTm/rIe+hgI5TgtEv4KsOzTB+cZtYVDe6fXg8xHI8n5DPftRPY17frfEJH0pGN0IkL/q2Vg9ptyks4y+ptZM/1YV8EXxs7qixMH1T3uA7pi4lw/x9RegjM3kZdkUIJXvQgG5/QHdhUDSBlYuVV/on9ZOmtf/0s1zQ68dBSUAAAAASUVORK5CYII=":"Tel",\
"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAoBAMAAAB+0KVeAAAAMFBMVEUAAACSkqSLkZyKkp2KkZyOl6GLkZyKkp2LkZ2Lkp2NlZ6LkpyKkp2LkZz///+Mkp266R64AAAAEHRSTlMAHKXl/xvt7Ke2Hbem5gFbHSN4EQAAAGBJREFUeAFjAAFGZRcoMApggAExFzgohAu2zIKxVvvABa8IwFiMvnBBFwYEk4AgAhASRGgfhIKjgvSP9/f/sAh+8SdC8IoAWDtqoj2yC8Za6QEXFEe4KBEuyIrIMuDUDwA2tjSIJ8c82gAAAABJRU5ErkJggg==":"Cellphone",\
"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAoCAYAAACM/rhtAAAEzElEQVR4Ae1YA7hrORB+a9u2bdu2bdu2DnrfSYrtvkyK565t27Zt2zvTM2m7tyenuc/K99XTyT/6Z5Je49bIWrVabWJf6vV9AR4+bvIEPOlF6n18/RU/f+8L9Ra+PuJHMBBfD+oqlOYdIcCCHKyJIK5FAD8ioH//9xDqOy+CNxDQBwS0++/4/ctBVu9z7733TjjMgWVEZWXc4PbGZpH6mrwTRGov8o4Qt0zS/T9C9Js6zKoN2MsvN8HC256EHYYJsH///Xd8X+hLW7zwHnpnXwzxBD3VFWb1lmjYUy26uobKm12l0rQYyltjZeq3QOrjKPeG1mjUdyKC+ytOC7iHvd+zVSzWpkEFr7Cln4eRXn1YpgwVGIb6BwbZbwjCCreYfImK1bmHeVJzyHGPv+v7SH2ye6VG6jKuyp/9fGXp4coKQp0ZFx385OVKszqAK69gkjgQsEfnUFXn8yWchcY8igXwCXEgpQa+hmG2snAzZW6cPJerTdm9KCj/iD85z/MdAZrQUnGk0k6tNlkQwSUo9wfJJz3IK74obcV6P49DWV4jIR/34z3/oMK0bkqFYJSHorRqWgHh5g+2AHkMvXhAKNRyxIm+0Bvi9xl8/FnvLAW1pJElAEnGoo5f6rqyale79yK4ihXdYZOhEKE3HjYWYxEdYY+G2gJl/6HwsyEfdYxcpPqmbfx9XUjqPa0cJtR5TD3/tMilGT2whZhvT+NGNvpNSyvT6xhFvfsMmCVRplCZg7zGBVRyq9LS9i0AQ5schZYB/mipXriEXfx8Shg801XICDeAevFmXqv97fkP6xk5qviE0MH1TMxFe3jhY/bEYOe2JsoLmI1p4HAp0K5i39mScuUxTuTzkxT0zsMirIArzW2ZCqacJR60GiLVTg391eoUCUkK77IHj7J4b++GhXk9vzNA5EHW+26aHA0ipnvZqvPnNO+gB05igH9jrx7PGWAExzPAG9NTAQIG+LhN0U/29sYFwoOqKzjWe00cYn1phw52JxtSsJHqO3WAUh2T+DsPrcT4rh4sFp+ayHArDblWcJhzxAzMEFvYLH0sVqQvSA0VPqSE2V0AUjSa5xXY2D6g6APNmcY6vCLy69hDA5OJvLRWg88kbO3iPdzwpU4AuYO9HHcwdTF/nVoEn9nDpd5iI55wmJh99kqfeHM4IDky+rSm9/RMdoU4mDYINVtewtIVdjQylJN0cEo2hPNVqKszub4Lmomn3YjS7uZsgrp3c5kFP00ja+bLu5og4RHMsxPioyWOWBJORVCvc0hfMB2BT3IE+HIEtS4Ziv+9sqFHqgvdKAEFGeC3dKa1VxwMtg6p2DGIWlr/T3Mi0VP7QR++wgI52Jmz8vn+0zVGrkifYRXk3hlIEHRspGsPum2gJOcxv23RcEEHIwSvaZilnASAqXp+HIzgXDOxZCSs2GtUW6VSaVKqUnOLkM1WZhjVMPJgygVDHIUj0ygHMsiVViJObCSzhM1GSU/SdNGsUHVvwrHReS7MqNr0wxwk9Ubqz+YeJX7QHaCSNOtR1VL1t127CViGejE+SjyJ8/XGcFpkfZ0nBXyRzH/qD77U/Dv5d8plfdhwDzuNWnXiFeoUGkK5S5ir37/qnhbqQz+C+/HzFXRrwBP4uDVS1n9bb9Gp6rNIkgAAAABJRU5ErkJggg==":"Email"\
}
output_title = ["user_name","Addr","Tel", "Cellphone", "Email", "Other"]

# Create a new instance of the Chrome driver
chrome_driver_path = "./chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)

# go to the nextdoor login page
driver.get("https://nextdoor.com/login/")



# find the element that's id attribute is :
inputUserEmail = driver.find_element_by_id("id_username")
inputPassword = driver.find_element_by_id("id_password")

# type in the login box:
inputUserEmail.send_keys(UserEmail)
inputPassword.send_keys(Password)

# submit the form 
inputPassword.submit()

# we have to wait for the page to refresh, the last thing that seems to be updated is the title
WebDriverWait(driver, 60).until(EC.title_contains("Nextdoor"))

driver.get("https://nextdoor.com/directory/")

WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".neighbor-name")))

neighbors = driver.find_elements_by_class_name('neighbor-name')
links = []
for neighbor in neighbors:
    links.append(neighbor.get_attribute('href'))

with open("./"+UserEmail+".txt","w",encoding='utf-8', errors='ignore') as out_f:
    out_f.write("\t".join(output_title)+"\n")

    for link in links:

        output_line = {}

        driver.get(link)

        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".profile-summary-name")))
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".info-box-list-container")))
        time.sleep(3)
        output_line['user_name'] = driver.find_element_by_class_name("profile-summary-name").text
        if EC.presence_of_element_located((By.CSS_SELECTOR, "info-box-list-container")):
            icons = driver.find_elements_by_class_name("info-box-list-item-icon")
            content = driver.find_elements_by_class_name("info-box-list-item-content")
            i = 0
            for icon in icons:
                icon = icon.get_attribute("src")
                if icon in info_cat_dic.keys():
                    info_cat = info_cat_dic[icon]
                else:
                    info_cat = "Other"+str(i)
                if info_cat not in output_line.keys():
                    output_line[info_cat] = content[i].text
                i += 1
        for info_cat in output_title:
            if info_cat not in output_line.keys():
                output_line[info_cat] = ""
            out_f.write(output_line[info_cat]+"\t")
        for key in output_line.keys():
            if "Other" in key:
                out_f.write(output_line[key]+"\t")
        out_f.write("\n")


driver.quit()