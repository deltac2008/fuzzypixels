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
    public partial class ASDetails : Form
    {
        private ListViewItem _li = new ListViewItem();

        public ASDetails(ListViewItem passedLi, int mode)
        {
            InitializeComponent();
            preFillType();

            _li = passedLi;
            //tbItem.Text = _li.Text;
            cbType.SelectedIndex = 0;
            tbAddress.Text = _li.SubItems[1].Text;
            tbCost.Text = _li.SubItems[2].Text;

            switch (mode)
            {
                case 0:
                    btnOK.Text = "Edit";
                    //btnOK.Width = 75;
                    break;
                case 1:
                    btnOK.Text = "Add";
                    //btnOK.Width = 50;
                    break;
            }
        }

        private void preFillType()
        {
            cbType.Items.Add("SMTP");
            cbType.Items.Add("POP");

            cbType.DropDownStyle = ComboBoxStyle.DropDownList;
        }

        private void btnCancel_Click(object sender, EventArgs e)
        {

        }

        private void btnOK_Click(object sender, EventArgs e)
        {
            _li.Text = cbType.SelectedItem.ToString();
            _li.SubItems[1].Text = tbAddress.Text;
            _li.SubItems[2].Text = tbCost.Text;
        }
    }
}
