using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace ModifyInterOrgConnector
{
    public partial class getFileLocation : Form
    {
        Form1 mainForm;

        public getFileLocation(Form1 mainForm)
        {
            this.mainForm = mainForm;
            InitializeComponent();
            btnCancel.DialogResult = DialogResult.Cancel;
            btnOK.DialogResult = DialogResult.OK;
        }

        private void btnFileBrowse_Click(object sender, EventArgs e)
        {
            openFD.ShowDialog();
            tbFileName.Text = openFD.FileName;
        }

        private void btnCancel_Click(object sender, EventArgs e)
        {
            // create new empty file
            mainForm.ConnectorFileName = "InterOrgSendConnector.csv";
            this.Close();
        }

        private void tbFileName_TextChanged(object sender, EventArgs e)
        {
            if (tbFileName.Text.Length > 0)
                btnOK.Enabled = true;
            else
                btnOK.Enabled = false;
        }

        private void btnOK_Click(object sender, EventArgs e)
        {
            // save details of file name and close
            mainForm.ConnectorFileName = tbFileName.Text.ToString();
            this.Close();
            //return DialogResult.OK;
        }
    }
}
