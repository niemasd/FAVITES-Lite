import { useSelector, useDispatch } from "react-redux";
import { setConfig } from "../../features/config/configSlice";
import { Typography } from "@mui/material";
import styles from "./Body.module.css";
import globalJSON from "../../files/global.json";

const Body = (props) => {
  const { className } = props;
  const config = useSelector((state) => state.config.value);
  const dispatch = useDispatch();
  const selected = useSelector((state) => state.selected.value);

  return (
    <div className={`${className} ${styles.Main}`}>
      <Typography variant="h4">{selected}</Typography>
      <br/>
      <Typography>{globalJSON.DESC[selected]}</Typography>
    </div>
  );
};

export default Body;
