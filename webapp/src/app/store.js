import { configureStore } from "@reduxjs/toolkit";
import configReducer from "../features/config/configSlice";
import selectedReducer from "../features/selected/selectedSlice"

export default configureStore({
  reducer: {
    config: configReducer,
    selected: selectedReducer
  },
});
