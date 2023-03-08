import { useSelector } from "react-redux";
import { Typography } from "@mui/material";
import {
  ModelCitation,
  ModelDescription,
  ModelProperties,
  ModelRequirements,
  ModelSelect,
  ParametersSelect,
} from "./BodyModules";
import styles from "./Body.module.css";
import globalJSON from "../../files/global.json";
import { textParse } from "../../utils/utils";

const Body = (props) => {
  const { className } = props;
  const config = useSelector((state) => state.config.value);
  const selected = useSelector((state) => state.selected.value);

  return (
    <div className={`${className} ${styles.Main}`}>
      {selected && (
        <>
          <Typography variant="h3">{selected}</Typography>
          <br />
          <Typography>{textParse(globalJSON.DESC[selected], "HTML")}</Typography>
          <br />
          <Typography variant="h4">Step 1: Choose Model</Typography>

          <ModelSelect />
        </>
      )}

      {config[selected] && config[selected]["model"] && (
        <>
          <ModelDescription />
          <ModelCitation />
          <ModelProperties />
          <ModelRequirements />

          {Object.keys(
            globalJSON.MODELS[selected][config[selected]["model"]].PARAM
          ).length !== 0 && (
            <>
              <Typography variant="h4">Step 2: Choose Parameters</Typography>
              <br />
              <ParametersSelect />
            </>
          )}
        </>
      )}
    </div>
  );
};

export default Body;
