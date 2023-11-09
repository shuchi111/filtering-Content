using System;
using System.Windows.Forms;

namespace JoeAutomotive
{
    public partial class Form1 : Form
    {
        // Constants for service charges
        private const double OilChangeCharge = 26;
        private const double LubeJobCharge = 18;
        private const double RadiatorFlushCharge = 30;
        private const double TransmissionFlushCharge = 80;
        private const double InspectionCharge = 15;
        private const double MufflerReplacementCharge = 100;
        private const double TireRotationCharge = 20;
        private const double LaborRate = 50;
        private const double TaxRate = 0.055;

        public Form1()
        {
            InitializeComponent();
        }

        // Value-returning methods

        private double CalculateOilLubeCharges()
        {
            double charges = 0;
            if (oilChangeCheckBox.Checked)
                charges += OilChangeCharge;
            if (lubeJobCheckBox.Checked)
                charges += LubeJobCharge;
            return charges;
        }

        private double CalculateFlushCharges()
        {
            double charges = 0;
            if (radiatorFlushCheckBox.Checked)
                charges += RadiatorFlushCharge;
            if (transmissionFlushCheckBox.Checked)
                charges += TransmissionFlushCharge;
            return charges;
        }

        private double CalculateMiscCharges()
        {
            double charges = 0;
            if (inspectionCheckBox.Checked)
                charges += InspectionCharge;
            if (mufflerReplacementCheckBox.Checked)
                charges += MufflerReplacementCharge;
            if (tireRotationCheckBox.Checked)
                charges += TireRotationCharge;
            return charges;
        }

        private double CalculateLaborCharges()
        {
            double laborHours;
            if (double.TryParse(laborTextBox.Text, out laborHours))
                return laborHours * LaborRate;
            return 0;
        }

        private double CalculatePartsCharges()
        {
            double partsCharges;
            if (double.TryParse(partsTextBox.Text, out partsCharges))
                return partsCharges;
            return 0;
        }

        private double CalculateTaxCharges(double chargeableAmount)
        {
            return chargeableAmount * TaxRate;
        }

        private double CalculateTotalCharges()
        {
            double totalCharges = 0;
            totalCharges += CalculateOilLubeCharges();
            totalCharges += CalculateFlushCharges();
            totalCharges += CalculateMiscCharges();
            totalCharges += CalculateLaborCharges();
            totalCharges += CalculatePartsCharges();
            totalCharges += CalculateTaxCharges(CalculatePartsCharges());
            return totalCharges;
        }

        // Void methods

        private void ClearCheckBoxes()
        {
            oilChangeCheckBox.Checked = false;
            lubeJobCheckBox.Checked = false;
            radiatorFlushCheckBox.Checked = false;
            transmissionFlushCheckBox.Checked = false;
            inspectionCheckBox.Checked = false;
            mufflerReplacementCheckBox.Checked = false;
            tireRotationCheckBox.Checked = false;
        }

        private void ClearTextAndLabels()
        {
            laborTextBox.Text = "";
            partsTextBox.Text = "";
            totalChargesLabel.Text = "";
            taxChargesLabel.Text = "";
        }

        private void clearButton_Click(object sender, EventArgs e)
        {
            ClearCheckBoxes();
            ClearTextAndLabels();
        }

        private void calculateButton_Click(object sender, EventArgs e)
        {
            double oilLubeCharges = CalculateOilLubeCharges();
            double flushCharges = CalculateFlushCharges();
            double miscCharges = CalculateMiscCharges();
            double laborCharges = CalculateLaborCharges();
            double partsCharges = CalculatePartsCharges();
            double taxCharges = CalculateTaxCharges(partsCharges);
            double totalCharges = CalculateTotalCharges();

            totalChargesLabel.Text = totalCharges.ToString("C");
            taxChargesLabel.Text = taxCharges.ToString("C");
        }
    }
}
