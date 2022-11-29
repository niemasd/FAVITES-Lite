import { useSelector, useDispatch } from "react-redux";
import { setConfig } from "../../features/config/configSlice";
import {
  Typography,
  FormControl,
  InputLabel,
  Select,
  MenuItem,
  TextField,
} from "@mui/material";
import globalJSON from "../../files/global.json";

export const ModelSelect = () => {
  const config = useSelector((state) => state.config.value);
  const selected = useSelector((state) => state.selected.value);
  const dispatch = useDispatch();

  const models = globalJSON["MODELS"][selected] || {};

  return (
    <FormControl variant="standard" sx={{ m: 1, minWidth: 120 }}>
      <InputLabel id="model-select-label">Model</InputLabel>
      <Select
        labelId="model-select"
        id="model-select"
        value={config[selected] ? config[selected]["model"] : ""}
        label="Model"
        onChange={(e) => {
          let newConfig = { ...config };
          newConfig[selected] = { model: e.target.value };
          console.log(newConfig);
          dispatch(setConfig(newConfig));
        }}
      >
        {/* <MenuItem value="">
          <em>Not Selected</em>
        </MenuItem> */}
        {Object.keys(models).map((model) => (
          <MenuItem key={model} value={model}>
            {model}
          </MenuItem>
        ))}
      </Select>
    </FormControl>
  );
};

export const ModelCitation = () => {
  const config = useSelector((state) => state.config.value);
  const selected = useSelector((state) => state.selected.value);

  const citation = globalJSON.MODELS[selected][config[selected]["model"]].CITE;

  if (citation) {
    return (
      <>
        <Typography variant="h5">Citation</Typography>
        <Typography>{citation}</Typography>
        <br />
      </>
    );
  }

  return <></>;
};

export const ModelDescription = () => {
  const config = useSelector((state) => state.config.value);
  const selected = useSelector((state) => state.selected.value);

  const description =
    globalJSON.MODELS[selected][config[selected]["model"]].DESC;

  if (description) {
    return (
      <>
        <Typography variant="h5">Description</Typography>
        <Typography>{description}</Typography>
        <br />
      </>
    );
  }

  return <></>;
};

export const ModelProperties = () => {
  const config = useSelector((state) => state.config.value);
  const selected = useSelector((state) => state.selected.value);

  const properties =
    globalJSON.MODELS[selected][config[selected]["model"]].PROP;

  if (properties) {
    return (
      <>
        <Typography variant="h5">Properties</Typography>
        <ul>
          {properties.map((prop) => (
            <li key={prop}>{prop}</li>
          ))}
        </ul>
        <br />
      </>
    );
  }

  return <></>;
};

export const ModelRequirements = () => {
  const config = useSelector((state) => state.config.value);
  const selected = useSelector((state) => state.selected.value);

  const properties =
    globalJSON.MODELS[selected][config[selected]["model"]].REQS;

  if (properties) {
    return (
      <>
        <Typography variant="h5">Properties</Typography>
        <ul>
          {Object.keys(properties).map((req) => (
            <li key={req}>
              {req}: {properties[req]}
            </li>
          ))}
        </ul>
        <br />
      </>
    );
  }

  return <></>;
};

// export const ModelParameters = () => {
//   const config = useSelector((state) => state.config.value);
//   const selected = useSelector((state) => state.selected.value);

//   const parameters =
//     globalJSON.MODELS[selected][config[selected]["model"]].PARAM;

//   if (parameters) {
//     return (
//       <>
//         <Typography variant="h5">Parameters</Typography>
//         <ul>
//           {Object.keys(parameters).map((param) => (
//             <li key={param}>
//               {param}
//               <ul>
//                 <li>Type: {parameters[param].TYPE}</li>
//                 <li>Description: {parameters[param].DESC}</li>
//               </ul>
//             </li>
//           ))}
//         </ul>
//         <br />
//       </>
//     );
//   }

//   return <></>;
// };

export const ParametersSelect = () => {
  const config = useSelector((state) => state.config.value);
  const selected = useSelector((state) => state.selected.value);
  const dispatch = useDispatch();

  const parameters =
    globalJSON.MODELS[selected][config[selected]["model"]].PARAM;

  if (parameters) {
    return (
      <>
        {Object.keys(parameters).map((param) => {
          /**
           * TODO: implement restrictions based on param type
           *
           * possible types:
           * - positive integer
           * - positive float
           * - probability
           * - non-negative float
           * - comma-separated list
           */

          return (
            <div key={param}>
              <TextField
                label={param}
                variant="standard"
                value={
                  config[selected]["param"]
                    ? config[selected]["param"][param] || ""
                    : ""
                }
                onChange={(e) => {
                  let newConfig = { ...config };
                  newConfig[selected] = {
                    ...newConfig[selected],
                    param: { ...newConfig[selected]["param"] },
                  };
                  newConfig[selected]["param"][param] = e.target.value;

                  dispatch(setConfig(newConfig));
                }}
              />
              <ul>
                <li>Type: {parameters[param].TYPE}</li>
                <li>Description: {parameters[param].DESC}</li>
              </ul>
            </div>
          );
        })}
      </>
    );
  }

  return <></>;
};
