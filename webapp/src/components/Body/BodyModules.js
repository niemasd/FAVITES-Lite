import { useSelector, useDispatch } from "react-redux";
import { setConfig } from "../../features/config/configSlice";
import {
  Typography,
  FormControl,
  InputLabel,
  Select,
  MenuItem,
} from "@mui/material";
import globalJSON from "../../files/global.json";

export const ModelSelect = () => {
  const config = useSelector((state) => state.config.value);
  const selected = useSelector((state) => state.selected.value);
  const dispatch = useDispatch();

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

          dispatch(setConfig(newConfig));
        }}
      >
        {/* <MenuItem value="">
          <em>Not Selected</em>
        </MenuItem> */}
        {Object.keys(globalJSON["MODELS"][selected]).map((model) => (
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
            <li>{prop}</li>
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

  const requirements =
    globalJSON.MODELS[selected][config[selected]["model"]].REQS;

  if (requirements) {
    return (
      <>
        <Typography variant="h5">Properties</Typography>
        <ul>
          {Object.keys(requirements).map((req) => (
            <li>
              {req}: {requirements[req]}
            </li>
          ))}
        </ul>
        <br />
      </>
    );
  }

  return <></>;
};
