import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Grid from '@material-ui/core/Grid';

// Account Settings Components
import { Hidden } from '@material-ui/core';
import XSFormField from './Display-xs-form.component';
import SMFormField from './Display-sm-form.component';

const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
  },
  container: {
    display: 'flex',
    flexWrap: 'wrap',
  },
  paper: {
    padding: theme.spacing(2),
    textAlign: 'center',
    color: theme.palette.text.secondary,
    flex: '1 0 auto',
    margin: theme.spacing(1),
  },
}));

export default function AccountSettings() {
  const classes = useStyles();

  return (
    <div className={classes.root}>
      <Grid container spacing={3}>
        <Hidden only='xs'>
          <SMFormField />
        </Hidden>
        <Hidden smUp mdUp lgUp xlUp>
          <XSFormField />
        </Hidden>
      </Grid>
    </div>
  );
}
