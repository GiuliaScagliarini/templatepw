import streamlit as st
from pag1 import main as  pag1
from pag_burger import main as  pag2
from pag3 import main as  pag3
from pag4 import main as  pag4
from pag5 import main as  pag5
#from pagxx import main as pagxx


def main():
	
	################ load logo from web #########################
	from PIL import Image
	import requests
	from io import BytesIO
	url='https://frenzy86.s3.eu-west-2.amazonaws.com/fav/bdl.png'
	response = requests.get(url)
	image = Image.open(BytesIO(response.content))
	st.title("FAV BIG DATALAB PW BiFor")
	st.image(image, caption='',use_column_width=True)

				
	pag_name = ["birra","burger","fritti","cocktail","bar"]
	
	OPTIONS = pag_name
	sim_selection = st.sidebar.selectbox('Seleziona la pagina', OPTIONS)

	if sim_selection == pag_name[0]:
		pag1()
	elif sim_selection == pag_name[1]:
		pag2()
	elif sim_selection == pag_name[2]:
		pag3()
	elif sim_selection == pag_name[3]:
		pag4()
	elif sim_selection == pag_name[4]:
		pag5()
	else:
		st.markdown("Something went wrong. We are looking into it.")


if __name__ == '__main__':
	main()