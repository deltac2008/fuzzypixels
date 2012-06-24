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
    public partial class dlgFilename : Form
    {
        Form1 mainForm;

        public dlgFilename(Form1 mainForm)
        {
            this.mainForm = mainForm;
            InitializeComponent();
            tbFilePath.Text = mainForm.ConnectorFileName.ToString();
            
        }

        private void btnOK_Click(object sender, EventArgs e)
        {
            this.Close();
        }
    }
}
