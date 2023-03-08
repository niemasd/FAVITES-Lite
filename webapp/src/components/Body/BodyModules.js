import { useSelector, useDispatch } from "react-redux";
import { setConfig } from "../../features/config/configSlice";
import { setStatuses } from "../../features/statuses/statusesSlice";
import {
  Typography,
  FormControl,
  InputLabel,
  Select,
  MenuItem,
  TextField,
} from "@mui/material";
import globalJSON from "../../files/global.json";
import { textParse, isValidParameter, status } from "../../utils/utils";
import { useEffect } from "react";

export const ModelSelect = () => {
  const config = useSelector((state) => state.config.value);
  const selected = useSelector((state) => state.selected.value);
  const dispatch = useDispatch();

  const models = globalJSON["MODELS"][selected] || {};

  const checkParams = (model) => {
    // Case 1: checking for errors
    const parameters = config[model]
      ? globalJSON.MODELS[model][config[model]["model"]].PARAM
      : null;

    let hasError = false;

    if (!parameters) return status.NOT_SELECTED;

    Object.keys(parameters).forEach((param) => {
      const val = config[model]["param"]
        ? config[model]["param"][param] || ""
        : "";

      const isError = !isValidParameter(val, parameters[param].TYPE);

      hasError = hasError || isError;
    });

    if (hasError) return status.ERROR;

    // Case 2: check for completeness
    let totalParams =
      globalJSON.MODELS[model][config[model]["model"]].PARAM;
    let totalParamCount = Object.keys(totalParams).length;

    let modelStatus = status.INCOMPLETE;

    // Checks if no params
    if (totalParamCount === 0) {
      modelStatus = status.COMPLETE;
    } else if (config[model]["param"]) {
      let completedParamCount = Object.keys(config[model]["param"]).length;
      if (completedParamCount === totalParamCount) {
        modelStatus = status.COMPLETE;
      }
    }

    return modelStatus;
  };

  const checkReqs = (model) => {
    let hasError = false;
    const requirements = config[model]
      ? globalJSON.MODELS[model][config[model]["model"]].REQS
      : null;

    // TODO: add check in error for model requirements
    if (!requirements) return checkParams(model);

    Object.keys(requirements).forEach((req) => {
      const expected = requirements[req];
      const actual = config[req] ? config[req]["model"] : null;

      const isError = expected !== actual;

      hasError = hasError || isError;
    });

    if (hasError) return status.ERROR;

    return checkParams(model);
  };

  useEffect(() => {
    let newStatuses = {}

    Object.keys(config).forEach((model) => {
      newStatuses[model] = checkReqs(model);
    })

    dispatch(setStatuses(newStatuses))
  // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [config]);

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
          newConfig[selected] = { model: e.target.value, "param": {}};
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
        <Typography>{textParse(description, "HTML")}</Typography>
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
            <li key={prop}>{textParse(prop, "HTML")}</li>
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
        <Typography variant="h5">Requirements</Typography>
        <ul>
          {Object.keys(requirements).map((req) => (
            <li key={req}>
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
          const val = config[selected]["param"]
            ? config[selected]["param"][param] || ""
            : "";

          const isError = !isValidParameter(val, parameters[param].TYPE);

          return (
            <div key={param}>
              <TextField
                error={isError}
                label={param}
                variant="standard"
                value={val}
                onChange={(e) => {
                  let newConfig = { ...config };
                  newConfig[selected] = {
                    ...newConfig[selected],
                    param: { ...newConfig[selected]["param"] },
                  };
                  // Remove the param from newConfig if user deletes entry from corresponding text box
                  if (e.target.value === "") {
                    delete newConfig[selected]["param"][param];
                  } else {
                    newConfig[selected]["param"][param] = e.target.value;
                  }
                  dispatch(setConfig(newConfig));
                }}
                helperText={isError ? "Invalid input" : ""}
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
