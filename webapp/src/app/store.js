import { configureStore } from "@reduxjs/toolkit";
import configReducer from "../features/config/configSlice";

export default configureStore({
  reducer: {
    config: configReducer,
  },
});
