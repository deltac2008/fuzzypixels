using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.IO;

namespace ModifyInterOrgConnector
{
    public partial class Form1 : Form
    {
        public string ConnectorFileName = "InterOrgSendConnector.csv";

        public Form1()
        {
            InitializeComponent();

            // read in any exising data
            readConnectorFile();
        }

        private bool readConnectorFile()
        {
            try
            {
                // read domain information from csv file
                StreamReader sr = new StreamReader(ConnectorFileName);
                string strLine = "";

                // clear all data from the listview then replace with file contents
                listView1.Items.Clear();

                string[] _values = null;
                while (!sr.EndOfStream)
                {
                    strLine = sr.ReadLine();
                    _values = strLine.Split(',');
                    ListViewItem lvi = new ListViewItem(_values[0].ToUpper());
                    lvi.SubItems.Add(_values[1]);
                    lvi.SubItems.Add(_values[2]);
                    listView1.Items.Add(lvi);
                }
                
                // close the file
                sr.Close();
                return true;
            }
            catch (System.Exception e)
            {
                //MessageBox.Show(e.Message);
                // if error then try to locate existing file or create a new file
                //dlgFilename dlgFN = new dlgFilename(this);
                //dlgFN.Show();
                return false;
            }
            finally
            {
            }
        }

        private void writeConnectorFile()
        {
            try
            {
                if (File.Exists(ConnectorFileName + ".bak"))
                    File.Delete(ConnectorFileName + ".bak");

                File.Move(ConnectorFileName, ConnectorFileName + ".bak");
                StreamWriter sw = new StreamWriter(ConnectorFileName);

                foreach (ListViewItem item in listView1.Items)
                {
                    sw.WriteLine(item.SubItems[0].Text.ToString() + ","
                        + item.SubItems[1].Text.ToString() + ","
                        + item.SubItems[2].Text.ToString());
                }
                sw.Close();
            }
            catch (System.Exception e)
            {
                // if error writing to file
                MessageBox.Show(e.Message);
            }
            finally
            {
            }
        }

        private void btnCancel_Click(object sender, EventArgs e)
        {
            // prompt to save any information if required

            // then quit app
            Application.Exit();
        }

        private void btnOK_Click(object sender, EventArgs e)
        {
            // Save any changes to file
            writeConnectorFile();

            // then close app
            Application.Exit();
        }

        private void btnAbout_Click(object sender, EventArgs e)
        {
            AboutBox1 dlgAbout = new AboutBox1();
            dlgAbout.Show();
        }

        private void btnAdd_Click(object sender, EventArgs e)
        {   
            // add a new entry
            ListViewItem lvi = new ListViewItem("aaa");
            lvi.SubItems.Add("aaa");
            lvi.SubItems.Add("aaa");
            //lvi.ImageIndex = 0;
            ASDetails dlg = new ASDetails(lvi, 1);
            dlg.ShowDialog();
        }

        private void btnEdit_Click(object sender, EventArgs e)
        {
            // edit selected entry
            if (object.Equals(listView1.SelectedItems.Count, 1))
            {
                ListViewItem lvi = listView1.SelectedItems[listView1.SelectedItems.Count - 1];
                ASDetails dlg = new ASDetails(lvi,0);
                dlg.ShowDialog();
            }
        }

        private void btnDelete_Click(object sender, EventArgs e)
        {
            // display confirmation prompt for deletion
            DialogResult result;
            result = MessageBox.Show("Delete the selected item(s)?", "Delete Confirmation", MessageBoxButtons.YesNo, MessageBoxIcon.Warning);

            if (result == DialogResult.Yes)
            {
                for (int i = listView1.SelectedItems.Count - 1; i >= 0; i--)
                {
                    ListViewItem li = listView1.SelectedItems[i];
                    listView1.Items.Remove(li);
                }
            }
        }

        private void btnConnectorFile_Click(object sender, EventArgs e)
        {
            // displays the current file path of the connector file
            dlgFilename dlgFN = new dlgFilename(this);
            dlgFN.Show();
        }

        private void listView1_SelectedIndexChanged(object sender, EventArgs e)
        {
            // enable delete option if one or more items are selected
            if (object.Equals(listView1.SelectedItems.Count, 0))
                btnDelete.Enabled = false;
            else
                btnDelete.Enabled=true;

            // enable edit option if only one item is selected
            if (object.Equals(listView1.SelectedItems.Count, 1))
                btnEdit.Enabled = true;
            else
                btnEdit.Enabled = false;
        }

        private void btnWriteFile_Click(object sender, EventArgs e)
        {
            // save current list
            writeConnectorFile();
        }

        private void btnReadFile_Click(object sender, EventArgs e)
        {
            // read list from file
            if (!readConnectorFile())
            {
                getFileLocation dlgGetFile = new getFileLocation(this);
                if (dlgGetFile.ShowDialog() == DialogResult.OK)
                    readConnectorFile();
            }
        }

    }
}
