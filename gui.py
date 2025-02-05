import flet as ft
import elements
import update
import read
from addnew import add_to_wl
import delete
import os
import pathlib

color1 = "#0f171f"
color2 = "#0b1b2b"
color3 = "#071636"
color4 = "#21354f"
color5 = "#476395"
color6 = "#798fb4"
color7 = ft.Colors.with_opacity(0.5, "#476395")
color8 = "#9cacca"
black1 = ft.Colors.with_opacity(0.4, "#000000")
black2 = ft.Colors.with_opacity(0.8, "#000000cc")
black3 = "#1b1b1b"
black4 = "#202020"
black5 = "#070B0F"


parent = pathlib.Path(__file__).parent.resolve()

if os.listdir(f"{parent}/watchlist") == []:
    with open("watchlist/control.txt", "w") as ctrlfile:
        ctrlfile.write("0\n")


watchlist = read.readAll()

target_modal = elements.new_modal()
addmodal = elements.addForm()


def handleAddModal(e: ft.ControlEvent):
    global addmodal
    e.page.open(addmodal[0])
    e.page.update()


def handleSaveEdit(e: ft.ControlEvent):
    global watchlist
    global wlgrid
    newtitle = target_modal[1].value
    newtarget = target_modal[2].value
    id = target_modal[0].key
    update.update_one(newtitle, newtarget, id)
    index = 0
    for w in watchlist:
        if w[-1] == id:
            index = watchlist.index(w)
    updated = read.read_one(id)
    buildwl(wlgrid, [updated], index)
    watchlist = read.readAll()
    e.page.close(target_modal[0])
    e.page.update()

target_modal[5].on_click = handleSaveEdit


def handleDeleteOne(e: ft.ControlEvent):
    global watchlist
    global target_modal
    global wlgrid
    id = target_modal[0].key
    for w in watchlist:
        if w[-1] == id:
            index = watchlist.index(w)
    watchlist.pop(index)
    wlgrid.controls.pop(index)
    delete.delete(id)
    e.page.close(target_modal[0])
    e.page.update()

target_modal[7].on_click = handleDeleteOne

def handleCardClick(e: ft.ControlEvent):
    global watchlist
    clickedCard = e.control
    index = wlgrid.controls.index(clickedCard.parent)
    vars = watchlist[index]
    target_modal[0].key = vars[-1]
    target_modal[1].value = vars[1]
    target_modal[2].value = vars[3]
    target_modal[3].value = vars[0]
    target_modal[4].src = vars[4]
    e.page.open(target_modal[0])
    e.page.update()


def handleOpenBrowser(e: ft.ControlEvent):
    e.page.launch_url(target_modal[3].value)

target_modal[6].on_click = handleOpenBrowser

def buildwl(grid, content, pos=-1):  
    if pos > -1:
        w = content[0]
        grid.controls[pos] = elements.card(w[-1], w[1], w[2], w[3], w[4], handleCardClick)
    else:
        for w in content:
            grid.controls.append(
                elements.card(w[-1], w[1], w[2], w[3], w[4], handleCardClick)
            )


def handleUpdateAll(e: ft.ControlEvent):
    global watchlist
    global wlgrid
    watchlist = update.update_all()
    wlgrid.controls = []
    buildwl(wlgrid, watchlist)
    e.page.update()


def handleAdd(e: ft.ControlEvent):
    global watchlist
    global addmodal
    e.page.close(addmodal[0])
    e.page.update()
    new = add_to_wl(
        addmodal[3].value,
        addmodal[1].value,
        addmodal[2].value
    )
    watchlist = read.readAll()
    buildwl(wlgrid, [new])
    
    e.page.update()

addmodal[4].on_click = handleAdd

wlgrid = ft.GridView(
    expand=True,
    runs_count=5,
    max_extent=150,
    child_aspect_ratio=1.0,
    spacing=10,
    run_spacing=10,
    height= 550
)



def main(page: ft.Page):

    page.window.min_height = 600
    page.window.height = 600
    page.window.min_width = 800
    page.window.width = 800

    page.padding = 20
    page.title = "fashionTracker"
    page.bgcolor = color2

    addNew = elements.button("add new")
    addNew.on_click = handleAddModal
    update_button = elements.button("update all")
    update_button.on_click = handleUpdateAll

    wl_header = ft.Container(
        bgcolor=ft.Colors.with_opacity(0.5, color3),
        padding=10,
        border=ft.border.all(1, color5),
        border_radius=6,
        content=ft.Row(
            controls=[
                ft.Text(
                    value="Watchlist",
                    expand=1,
                    style=ft.TextStyle(
                        size=page.height/30, 
                        color=color8
                    )
                ),
                addNew,
                update_button,
            ]
        )
    )

    

    right_side = ft.Column(
        controls=[
            wl_header,
            wlgrid
        ]
    )

    page.add(addmodal[0])
    page.add(target_modal[0])

    if watchlist:
        buildwl(wlgrid, watchlist)

    main_row = ft.Row()
    main_row.alignment = ft.alignment.top_center

    page.add(
        ft.Row(
            alignment=ft.MainAxisAlignment.START,
            vertical_alignment=ft.CrossAxisAlignment.START,
            controls=[
                ft.Container(
                    expand=1,
                    content=right_side
                )
            ]
            
        )
    )

ft.app(main)