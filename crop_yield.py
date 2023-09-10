import streamlit as st
import pickle
from streamlit_option_menu import option_menu

#loading the saved model
yield_model=pickle.load(open('C:/Users/FRANK/Desktop/Crop Yield Prediction/yield_model.sav','rb'))

crop_model=pickle.load(open('C:/Users/FRANK/Desktop/Crop_Recommendation System/crop_recommendation.sav','rb'))


with st.sidebar:
	selected=option_menu("CROP PREDICTION SYSTEMS",
			['Yield Prediction','Crop Recommendation System'],default_index=0)

if(selected == 'Yield Prediction'):
	st.title("CROP YIELD PREDICTION SYSTEM")	
	st.write("Which crop would you like to predict?")
	col1,col2,col3=st.columns(3)
	with col1:
		if st.checkbox("Cassava"):
    			Item_Cassava=1
		else:
        		Item_Cassava=0
	with col2:
		if st.checkbox("Maize"):
        		Item_Maize=1
		else:
        		Item_Maize=0
	with col3:
		if st.checkbox("Plaintains and Others"):
        		Item_Plantains=1
		else:
        		Item_Plantains=0
	with col1:
		if st.checkbox("Potatoes"):
        		Item_Potatoes=1
		else:
        		Item_Potatoes=0
		
	with col2:
		if st.checkbox("Rice Paddy"):
        		Item_Rice=1
		else:
        		Item_Rice=0
		
	with col3:
		if st.checkbox("Sorghum"):
        		Item_Sorghum=1
		else:
        		Item_Sorghum=0
		
	with col1:
		if st.checkbox("Soybeans"):
        		Item_Soybeans=1
		else:
        		Item_Soybeans=0
		
	with col2:
		if st.checkbox("SweetPotatoes"):
        		Item_Sweetpotatoes=1
		else:
        		Item_Sweetpotatoes=0
		
	with col3:
		if st.checkbox("Wheat"):
        		Item_Wheat=1
		else:
       	 		Item_Wheat=0
		
	with col1:
		if st.checkbox("Yams"):
        		Item_Yams=1
		else:
        		Item_Yams=0
		

	st.write("Enter the following parameters:")
	average_rain_fall_mm_per_year=st.number_input("Average rainfall in mm per year")
	pesticides_tonnes=st.number_input("Pesticides in Tonnes")
	avg_temp=st.number_input("Average Temperature")
	#code for prediction
	yield_prediction=''


	if st.button("PREDICT YIELD IN HG/HA"):
		yield_prediction=yield_model.predict([[average_rain_fall_mm_per_year,pesticides_tonnes,avg_temp,Item_Cassava,Item_Maize,Item_Plantains,
						Item_Potatoes,Item_Rice,Item_Sorghum,Item_Soybeans,Item_Sweetpotatoes,Item_Wheat,Item_Yams]])
		st.success(yield_prediction)
		st.write("The total yield prediction is",yield_prediction,"in HG/HA")

if (selected=='Crop Recommendation System'):
	st.title("CROP RECOMMENDATION SYSTEM")
	col1,col2=st.columns(2)
	with col1:
		N=st.text_input('Nitrogen Content in the soil')

	with col2:
		P=st.text_input('Phosphorous Content in the soil')

	with col1:
		K=st.text_input('Potassium Content in the soil')

	with col2:
		temperature=st.text_input('Temperature in Degrees Celcius')

	with col1:
		humidity=st.text_input('Relative Humidity in percentage')

	with col2:
		ph=st.text_input('PH value of the soil')

	with col1:
		rainfall=st.text_input('Rainfall in mm')


	st.text('Which crop is recommended?')

	if st.button("Predict Crop"):
		crop_prediction=crop_model.predict([[N,P,K,temperature,humidity,ph,rainfall]])
		st.success(crop_prediction)
		st.write("The recommended crop to be grown is:",crop_prediction)







