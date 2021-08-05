﻿
namespace GPSDataTool
{
    partial class FrmMain
    {
        /// <summary>
        /// 필수 디자이너 변수입니다.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// 사용 중인 모든 리소스를 정리합니다.
        /// </summary>
        /// <param name="disposing">관리되는 리소스를 삭제해야 하면 true이고, 그렇지 않으면 false입니다.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form 디자이너에서 생성한 코드

        /// <summary>
        /// 디자이너 지원에 필요한 메서드입니다. 
        /// 이 메서드의 내용을 코드 편집기로 수정하지 마세요.
        /// </summary>
        private void InitializeComponent()
        {
            this.components = new System.ComponentModel.Container();
            this.label3 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.label1 = new System.Windows.Forms.Label();
            this.TxtSubscriptionTopic = new System.Windows.Forms.TextBox();
            this.TxtClientID = new System.Windows.Forms.TextBox();
            this.TxtConnectionString = new System.Windows.Forms.TextBox();
            this.BtnDisconnect = new System.Windows.Forms.Button();
            this.BtnConnect = new System.Windows.Forms.Button();
            this.RtbSubscr = new System.Windows.Forms.RichTextBox();
            this.Timer = new System.Windows.Forms.Timer(this.components);
            this.statusStrip1 = new System.Windows.Forms.StatusStrip();
            this.LblResult = new System.Windows.Forms.ToolStripStatusLabel();
            this.statusStrip1.SuspendLayout();
            this.SuspendLayout();
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(6, 73);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(111, 12);
            this.label3.TabIndex = 1;
            this.label3.Text = "Subscription Topic";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(65, 41);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(52, 12);
            this.label2.TabIndex = 2;
            this.label2.Text = "Client ID";
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(12, 9);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(105, 12);
            this.label1.TabIndex = 3;
            this.label1.Text = "Connection String";
            // 
            // TxtSubscriptionTopic
            // 
            this.TxtSubscriptionTopic.Location = new System.Drawing.Point(122, 71);
            this.TxtSubscriptionTopic.Name = "TxtSubscriptionTopic";
            this.TxtSubscriptionTopic.Size = new System.Drawing.Size(446, 21);
            this.TxtSubscriptionTopic.TabIndex = 4;
            this.TxtSubscriptionTopic.Text = "gps01/machine1/data/";
            // 
            // TxtClientID
            // 
            this.TxtClientID.Location = new System.Drawing.Point(123, 39);
            this.TxtClientID.Name = "TxtClientID";
            this.TxtClientID.Size = new System.Drawing.Size(446, 21);
            this.TxtClientID.TabIndex = 5;
            this.TxtClientID.Text = "SUBSCR01";
            // 
            // TxtConnectionString
            // 
            this.TxtConnectionString.Location = new System.Drawing.Point(123, 6);
            this.TxtConnectionString.Name = "TxtConnectionString";
            this.TxtConnectionString.Size = new System.Drawing.Size(446, 21);
            this.TxtConnectionString.TabIndex = 6;
            this.TxtConnectionString.Text = "210.119.12.94";
            // 
            // BtnDisconnect
            // 
            this.BtnDisconnect.Location = new System.Drawing.Point(692, 56);
            this.BtnDisconnect.Name = "BtnDisconnect";
            this.BtnDisconnect.Size = new System.Drawing.Size(101, 36);
            this.BtnDisconnect.TabIndex = 7;
            this.BtnDisconnect.Text = "Disconnect";
            this.BtnDisconnect.UseVisualStyleBackColor = true;
            this.BtnDisconnect.Click += new System.EventHandler(this.BtnDisconnect_Click);
            // 
            // BtnConnect
            // 
            this.BtnConnect.Location = new System.Drawing.Point(585, 56);
            this.BtnConnect.Name = "BtnConnect";
            this.BtnConnect.Size = new System.Drawing.Size(101, 36);
            this.BtnConnect.TabIndex = 8;
            this.BtnConnect.Text = "Connect";
            this.BtnConnect.UseVisualStyleBackColor = true;
            this.BtnConnect.Click += new System.EventHandler(this.BtnConnect_Click);
            // 
            // RtbSubscr
            // 
            this.RtbSubscr.Location = new System.Drawing.Point(14, 98);
            this.RtbSubscr.Name = "RtbSubscr";
            this.RtbSubscr.Size = new System.Drawing.Size(774, 340);
            this.RtbSubscr.TabIndex = 9;
            this.RtbSubscr.Text = "";
            // 
            // statusStrip1
            // 
            this.statusStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.LblResult});
            this.statusStrip1.Location = new System.Drawing.Point(0, 428);
            this.statusStrip1.Name = "statusStrip1";
            this.statusStrip1.Size = new System.Drawing.Size(800, 22);
            this.statusStrip1.TabIndex = 10;
            this.statusStrip1.Text = "statusStrip1";
            // 
            // LblResult
            // 
            this.LblResult.Name = "LblResult";
            this.LblResult.Size = new System.Drawing.Size(14, 17);
            this.LblResult.Text = "0";
            // 
            // FrmMain
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(7F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.statusStrip1);
            this.Controls.Add(this.RtbSubscr);
            this.Controls.Add(this.BtnDisconnect);
            this.Controls.Add(this.BtnConnect);
            this.Controls.Add(this.TxtSubscriptionTopic);
            this.Controls.Add(this.TxtClientID);
            this.Controls.Add(this.TxtConnectionString);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Name = "FrmMain";
            this.Text = "GPS Device";
            this.statusStrip1.ResumeLayout(false);
            this.statusStrip1.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.TextBox TxtSubscriptionTopic;
        private System.Windows.Forms.TextBox TxtClientID;
        private System.Windows.Forms.TextBox TxtConnectionString;
        private System.Windows.Forms.Button BtnDisconnect;
        private System.Windows.Forms.Button BtnConnect;
        private System.Windows.Forms.RichTextBox RtbSubscr;
        private System.Windows.Forms.Timer Timer;
        private System.Windows.Forms.StatusStrip statusStrip1;
        private System.Windows.Forms.ToolStripStatusLabel LblResult;
    }
}

