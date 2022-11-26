def pars_data(header_img: str, full_name: str, sub_title: str, linkedin_link: str, github_nickname: str):
    template = f'''
<div align="center">
<img src="{header_img}" width="350"/>
<h1>{full_name}</h1>
<h3>{sub_title}</h3>
</div>

<details open align="center"> 
<summary><h2>Social links</h2>  <img src="https://cdn-icons-png.flaticon.com/512/1232/1232859.png" width="40"></summary>

[![Linkedin Badge](https://img.shields.io/badge/linkedin-profile-blue?style=for-the-badge&logo=LinkedIn)]({linkedin_link})

</details>

<details close align="center"> 
<summary><h2>Languages</h2>  <img src="https://cdn-icons-png.flaticon.com/512/1230/1230137.png?w=826&t=st=1669474578~exp=1669475178~hmac=4ddfe461bba8521890670e6434d6b475a3f6f36c0dcee7a55c306110d5fcf1de" width="30"></summary>

<img src="https://img.shields.io/badge/HLVL-Python-green?style=for-the-badge&logo=Python&logoColor=yellow"/><br/> <!--python-->

</details>

<div align="center" >


<br/>
<picture>
<source media="(prefers-color-scheme: dark)" srcset="https://streak-stats.demolab.com?user={github_nickname}&theme=dark&hide_border=true&date_format=j%20M%5B%20Y%5D&background=00000000&sideNums=DD6F20&currStreakLabel=DD2727&sideLabels=DD2727&currStreakNum=DD2727" />
<img src="https://streak-stats.demolab.com?user={github_nickname}&theme=dark&hide_border=true&date_format=j%20M%5B%20Y%5D&background=00000000&sideNums=DD6F20&currStreakLabel=DD2727&sideLabels=DD2727&currStreakNum=DD2727" />
</picture>
</div>'''
    return template


def get_input(header_img: str, full_name: str, sub_title: str, linkedin_link: str, github_nickname: str):
    result = pars_data(header_img=header_img,
                       full_name=full_name,
                       sub_title=sub_title,
                       linkedin_link=linkedin_link,
                       github_nickname=github_nickname)
    return result
