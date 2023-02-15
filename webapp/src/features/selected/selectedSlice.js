import { createSlice } from "@reduxjs/toolkit";

export const selectedSlice = createSlice({
  name: "selected",
  initialState: {
    value: "",
  },
  reducers: {
    setSelected: (state, action) => {
      state.value = action.payload;
    },
  },
});

// Action creators are generated for each case reducer function
export const { setSelected } = selectedSlice.actions;

export default selectedSlice.reducer;
