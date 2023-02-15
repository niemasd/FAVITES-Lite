import { createSlice } from "@reduxjs/toolkit";

export const statusesSlice = createSlice({
  name: "statuses",
  initialState: {
    value: {},
  },
  reducers: {
    setStatuses: (state, action) => {
      state.value = action.payload;
    },
  },
});

// Action creators are generated for each case reducer function
export const { setStatuses } = statusesSlice.actions;

export default statusesSlice.reducer;
