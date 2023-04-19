import React, { useState } from "react";
import { Button } from "@mui/material";
import styles from "./Header.module.css";
import globalJSON from "../../files/global.json";
import ImportModal from "./ImportModal";
import ExportModal from "./ExportModal";

const Header = (props) => {
  const [openExport, setOpenExport] = useState(false);
  const [openImport, setOpenImport] = useState(false);

  const { className } = props;

  return (
    <>
      <div className={`${className} ${styles.Main}`}>
        <h1 className={styles.Title}>
          FAVITES-Lite <span className={styles.AltText}>Config Designer</span> v
          {globalJSON["VERSION"]}
        </h1>
        <div className={styles.ButtonRow}>
          <Button
            variant="contained"
            onClick={() => {
              setOpenImport(true);
            }}
            className={styles.Button}
          >
            Import
          </Button>
          <Button
            variant="contained"
            onClick={() => {
              setOpenExport(true);
            }}
            className={styles.Button}
          >
            Export
          </Button>
        </div>
      </div>
      <ExportModal open={openExport} setOpen={setOpenExport} />
      <ImportModal open={openImport} setOpen={setOpenImport} />
    </>
  );
};

export default Header;
