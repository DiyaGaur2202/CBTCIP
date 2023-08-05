from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet

DATA = [
    [ "Date" , "Phone", "Quantity", " Total Price (Rs.)" ],
    [
        "19/05/2023",
        "Iphone 13",
        "1",
        "70,000.00/-",
    ],
    [ "19/05/2023", "Charger", "1", "5000.00/-"],
    [ "Sub Total", "", "", "75,000.00/-"],
    [ "Discount", "", "", "-2000.00/-"],
    [ "Total", "", "", "73000.00/-"],
]

pdf = SimpleDocTemplate( "receipt.pdf" , pagesize = A4 )

styles = getSampleStyleSheet()

title_style = styles[ "Heading1" ]

title_style.alignment = 1

title = Paragraph( "iCorner" , title_style )


style = TableStyle(
    [
        ( "BOX" , ( 0, 0 ), ( -1, -1 ), 1 , colors.black ),
        ( "GRID" , ( 0, 0 ), ( 4 , 4 ), 1 , colors.black ),
        ( "BACKGROUND" , ( 0, 0 ), ( 3, 0 ), colors.red ),
        ( "TEXTCOLOR" , ( 0, 0 ), ( -1, 0 ), colors.whitesmoke ),
        ( "ALIGN" , ( 0, 0 ), ( -1, -1 ), "CENTER" ),
        ( "BACKGROUND" , ( 0 , 1 ) , ( -1 , -1 ), colors.beige ),
    ]
)

table = Table( DATA , style = style )

pdf.build([ title , table ])


