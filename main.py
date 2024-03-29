import acoup
import insideofknoxville
import datetime

from newspaper import Newspaper

start_date = datetime.datetime(2024, 2, 28)
end_date = datetime.datetime(2024, 2, 29)

html_header = """<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>CoffeeBadgerPress</title>
    <meta name="viewport" content="width=device-width">
    <style>
        img[class^="wp-image-"], [class^="size-large"] {
            height: auto;
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 100%;
        }
        figure[class^="wp-caption"] {
            max-width: fit-content;
        }
       @font-face {
    font-family: built;
    src: url(built\ titling\ sb.woff);
}
body{
    font-family: 'Times New Roman', Times, serif;
    font-weight: bold;
    font-size: 14px;
    color: #2f2f2f;
    background-color: rgb(252, 247, 225);
}
header{
    font-family: built;
    font-weight: 900;
    font-size: 80px;
    text-transform: uppercase;
    display: inline-block;
    line-height: 72px;
    
    letter-spacing: 8px;
    color:#5b5050;
}

p{
    margin-top: 0;
    margin-bottom: 20px;
}
.head{
    text-align: center;
    position: relative;
}

.title{
    text-align:center;
}

.subhead{
    text-transform: uppercase;
    border-bottom: 2px solid #2f2f2f;
    border-top: 2px solid #2f2f2f;
    padding: 12px 0 12px 0;

}


.content{
    font-size: 0;
    line-height: 0;
    word-spacing: -.31em;
    display: inline-block;
    margin: 30px 2% 0 2%;
}
.columns{
    text-align: left;
}

.column{
    font-size: 14px;
    line-height: 20px;
    display: inline-block;
    padding: 0 1% 0 1%;
    vertical-align: top;
    margin-bottom: 50px;
    transition: all .7s;
    column-count: 3;
    column-rule-style:groove;
    height: auto;
}

.column + .column { 
  border-left: 1px solid #2f2f2f;
}
.column .headline{
    text-align: center;
    line-height: normal;
    font-family: 'Playfair Display', serif;
    display: block;
    margin: 0 auto;
}
.column .headline.hl1{
    font-weight: 700;
    font-size: 30px;
    text-transform: uppercase;
    padding: 10px 0 10px 0;
}

.column .headline.hl2{
    font-weight: 400;
    font-style: italic;
    font-size: 24px;
    box-sizing: border-box;
    padding: 10px 0 10px 0;
}

.column .headline.hl2:before{
    border-top: 1px solid #2f2f2f;
    content: '';
    width: 100px;
    height: 7px;
    display: block;
    margin: 0 auto;
}

.collumn .headline.hl2:after{
    border-bottom: 1px solid #2f2f2f;
    content: '';
    width: 100px;
    height: 13px;
    display: block;
    margin: 0 auto;
}

.column .headline.hl3{
    font-weight: 400;
    font-style: italic;
    font-size: 36px;
    box-sizing: border-box;
    padding: 10px 0 10px 0;
}
.column .headline.hl4{
    font-weight: 700;
    font-size: 12px;
    box-sizing: border-box;
    padding: 10px 0 10px 0;
}
.column .headline.hl4:before{
    border-top: 1px solid #2f2f2f;
    content: '';
    width: 100px;
    height: 7px;
    display: block;
    margin: 0 auto;
}
.column .headline.hl4:after{
    border-bottom: 1px solid #2f2f2f;
    content: '';
    width: 100px;
    height: 10px;
    display: block;
    margin: 0 auto;
}

.column .headline.hl5{
    font-weight: 400;
    font-size: 42px;
    text-transform: uppercase;
    font-style: italic;
    box-sizing: border-box;
    padding: 10px 0 10px 0;
}
.column .headline.hl6{
    font-weight: 400;
    font-size: 18px;
    box-sizing: border-box;
    padding: 10px 0 10px 0;
}
.column .headline.hl6:before{
    border-top: 1px solid #2f2f2f;
    content: '';
    width: 100px;
    height: 7px;
    display: block;
    margin: 0 auto;
}
.column .headline.hl6:after{
    border-bottom: 1px solid #2f2f2f;
    content: '';
    width: 100px;
    height: 10px;
    display: block;
    margin: 0 auto;

}
.column .headline.hl7{
    font-weight: 700;
    font-size: 12px;
    box-sizing: border-box;
    display: block;
    padding: 10px 0 10px 0;
}
.column .headline.hl8{
    font-weight: 700;
    font-size: 12px;
    box-sizing: border-box;
    padding: 10px 0 10px 0;
}
.column .headline.hl9{
    font-weight: 700;
    font-size: 12px;
    box-sizing: border-box;
    padding: 10px 0 10px 0;
}
.column .headline.hl10{
    font-weight: 700;
    font-size: 12px;
    box-sizing: border-box;
    padding: 10px 0 10px 0;
}
.column .citation{
    font-family: 'Playfair Display', serif;
    font-size: 36px;
    line-height: 44px;
    text-align: center;
    font-weight: 400;
    display: block;
    margin: 40px 0 40px 0;
    font-feature-settings: "liga", "dlig";

}
.column .citation:before{
    border-top: 1px solid #2f2f2f;
    content: '';
    width: 100px;
    height: 16px;
    display: block;
    margin: 0 auto;
}
.column .citation:after{
    border-bottom: 1px solid #2f2f2f;
    content: '';
    width: 100px;
    height: 16px;
    display: block;
    margin: 0 auto;
}
.column .figure {
	  margin: 0 0 20px;
}
.column .figcaption{
	font-style: italic;
	font-size: 12px;
}
</style>
</head>
"""
html_header2 = f"""
<body>
<div class="head">
    <div class="headerobjectswrapper">
        <header>Coffee Badger Press</header>
    </div>
    <div class="subhead">Knoxville, TN: {start_date.strftime("%m/%d/%Y")} - {end_date.strftime("%m/%d/%Y")}</div>
</div>
<div class="content">
"""

html_end = "</body> </html>"

newspaper = Newspaper()
#newspaper = acoup.getArticles(newspaper, start_date, end_date)
newspaper = insideofknoxville.getArticles(newspaper, start_date, end_date)
html_art = []
for article in newspaper.articles:
    # Access the attributes of each article
    article_date = article.date
    article_title = article.title
    article_author = article.author
    article_content = article.content
    html_art.append(f"""<div class="collumn">
        <div class="head"><span class="headline hl3">
        {article_title}</span><p><span class="headline hl4">
        by {article_author}</span></p></div>
        {''.join(article_content)}
    </div>""")

html_art_string = ''.join(html_art)
html_content = html_header + html_header2 + html_art_string + html_end

# Specify the file path where you want to save the HTML file
file_path = "output.html"

# Open the file in write mode and write the HTML content to it
with open("output.html", "w", encoding="utf-8") as file:
    # Write the HTML content to the file
    file.write(html_content)
print("HTML file has been created successfully!")



