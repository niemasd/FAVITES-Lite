import { createSlice } from '@reduxjs/toolkit'

export const configSlice = createSlice({
  name: 'config',
  initialState: {
    value: {},
  },
  reducers: {
    setConfig: (state, action) => {
      state.value = action.payload;
    }
  },
})

// Action creators are generated for each case reducer function
export const { setConfig } = configSlice.actions

export default configSlice.reducer