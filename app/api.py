from fastapi import FastAPI
from models.Param import Param
import pickle
import warnings

app = FastAPI()

# app.include_router(params.router, tags=["Params"], prefix="/params")
# app.include_router(users.router, tags=["Users"], prefix="/users")
# app.include_router(predicts.router, tags=["Predict"], prefix="/predict")
# app.include_router(devices.router, tags=["Devices"], prefix="/devices")
LABEL = ["jagung", "bawang merah"]

@app.get("/")
def read_root():
    try:
        # db.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
        return { "success": True }
    except Exception as e:
        print(e)

        LABEL = ["jagung", "bawang merah"]

@app.post("/predict")
async def predict(param: Param):
    warnings.filterwarnings("ignore", message="X does not have valid feature names")
    pickle_in = open('model.pkl','rb')
    model = pickle.load(pickle_in)
    pre = model.predict_proba([[param.env_hum, param.soil_con, param.soil_hum, param.soil_nitro, param.soil_ph, param.soil_phos, param.soil_pot, param.soil_salin, param.soil_tds, param.soil_temp, param.env_temp]])
    result_list = [{'label': LABEL[i], 'value': val * 100} for i, val in enumerate(pre[0].tolist())]
    sorted_list = sorted(result_list, key=lambda x: x['value'], reverse=True)

    results = {}
    count = 0
    for i in sorted_list:
        results[count + 1] = sorted_list[count]
        count = count + 1
    return results