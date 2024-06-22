import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import scrolledtext
from tkcalendar import DateEntry
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle
from reportlab.lib import colors

class CVGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CV Generator")

        # Main frame
        main_frame = tk.Frame(self.root, bg="black")
        main_frame.pack(padx=20, pady=20)

        # Contact Information Frame
        contact_frame = tk.LabelFrame(main_frame, text="Contact Information", padx=10, pady=10)
        contact_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nw")

        # Labels and Entries for Contact Information
        tk.Label(contact_frame, text="Full Name:").grid(row=0, column=0, sticky="w")
        self.contact_full_name_entry = tk.Entry(contact_frame, width=40)
        self.contact_full_name_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        tk.Label(contact_frame, text="Address:").grid(row=1, column=0, sticky="w")
        self.contact_address_entry = tk.Entry(contact_frame, width=40)
        self.contact_address_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        tk.Label(contact_frame, text="Phone Number:").grid(row=2, column=0, sticky="w")
        self.contact_phone_entry = tk.Entry(contact_frame, width=40)
        self.contact_phone_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        tk.Label(contact_frame, text="Email Address:").grid(row=3, column=0, sticky="w")
        self.contact_email_entry = tk.Entry(contact_frame, width=40)
        self.contact_email_entry.grid(row=3, column=1, padx=5, pady=5, sticky="w")

        tk.Label(contact_frame, text="LinkedIn Profile:").grid(row=4, column=0, sticky="w")
        self.contact_linkedin_entry = tk.Entry(contact_frame, width=40)
        self.contact_linkedin_entry.grid(row=4, column=1, padx=5, pady=5, sticky="w")

        tk.Label(contact_frame, text="Website/Portfolio:").grid(row=5, column=0, sticky="w")
        self.contact_website_entry = tk.Entry(contact_frame, width=40)
        self.contact_website_entry.grid(row=5, column=1, padx=5, pady=5, sticky="w")

        # Education Frame
        education_frame = tk.LabelFrame(main_frame, text="Education", padx=10, pady=10)
        education_frame.grid(row=0, column=1, padx=10, pady=10, rowspan=1, columnspan=3)

        # Treeview for displaying education details
        self.education_tree = ttk.Treeview(education_frame, columns=("Institution", "Degree", "Field", "Date", "Honors"), show='headings', height=5)
        self.education_tree.heading("Institution", text="Institution")
        self.education_tree.heading("Degree", text="Degree")
        self.education_tree.heading("Field", text="Field of Study")
        self.education_tree.heading("Date", text="Graduation Date")
        self.education_tree.heading("Honors", text="Honors")
        self.education_tree.grid(row=0, column=0, columnspan=3, padx=5, pady=5, sticky="nw")

        # Buttons for adding, deleting, and editing education details
        self.add_edu_btn = tk.Button(education_frame, text="Add", command=self.add_education)
        self.add_edu_btn.grid(row=1, column=0, padx=5, pady=5)

        self.edit_edu_btn = tk.Button(education_frame, text="Edit", command=self.edit_education)
        self.edit_edu_btn.grid(row=1, column=1, padx=5, pady=5)

        self.delete_edu_btn = tk.Button(education_frame, text="Delete", command=self.delete_education)
        self.delete_edu_btn.grid(row=1, column=2, padx=5, pady=5)

        # Work Experience Frame
        work_frame = tk.LabelFrame(main_frame, text="Work Experience", padx=10, pady=10)
        work_frame.grid(row=1, column=1, padx=10, pady=10, sticky="nsew", columnspan=3)

        # Treeview for displaying work experience details
        self.work_tree = ttk.Treeview(work_frame, columns=("Job Title", "Company", "Location", "Dates", "Responsibilities"), show='headings', height=5)
        self.work_tree.heading("Job Title", text="Job Title")
        self.work_tree.heading("Company", text="Company")
        self.work_tree.heading("Location", text="Location")
        self.work_tree.heading("Dates", text="Dates of Employment")
        self.work_tree.heading("Responsibilities", text="Responsibilities and Achievements")
        self.work_tree.grid(row=0, column=0, columnspan=3, padx=5, pady=5, sticky="nsew")

        # Buttons for adding, deleting, and editing work experience details
        self.add_work_btn = tk.Button(work_frame, text="Add", command=self.add_work_experience)
        self.add_work_btn.grid(row=1, column=0, padx=5, pady=5)

        self.edit_work_btn = tk.Button(work_frame, text="Edit", command=self.edit_work_experience)
        self.edit_work_btn.grid(row=1, column=1, padx=5, pady=5)

        self.delete_work_btn = tk.Button(work_frame, text="Delete", command=self.delete_work_experience)
        self.delete_work_btn.grid(row=1, column=2, padx=5, pady=5)

        # Skills Frame
        skills_frame = tk.LabelFrame(main_frame, text="Skills", padx=10, pady=10)
        skills_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsw")

        # Technical Skills
        tk.Label(skills_frame, text="Technical\nSkills:").grid(row=0, column=0, sticky="w")
        self.tech_skills_text = scrolledtext.ScrolledText(skills_frame, width=30, height=3, wrap=tk.WORD)
        self.tech_skills_text.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        # Soft Skills
        tk.Label(skills_frame, text="Soft Skills:").grid(row=1, column=0, sticky="w")
        self.soft_skills_text = scrolledtext.ScrolledText(skills_frame, width=30, height=3, wrap=tk.WORD)
        self.soft_skills_text.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

        # Languages
        tk.Label(skills_frame, text="Languages:").grid(row=2, column=0, sticky="w")
        self.languages_text = scrolledtext.ScrolledText(skills_frame, width=31, height=3, wrap=tk.WORD)
        self.languages_text.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")

        # Reference Frame
        reference_frame = tk.LabelFrame(main_frame, text="Reference", padx=10, pady=10)
        reference_frame.grid(row=2, column=0, padx=10, pady=10, sticky="nsw")

        # Labels and Entries for Reference Information
        tk.Label(reference_frame, text="Full Name: ").grid(row=0, column=0, sticky="w")
        self.ref_full_name_entry = tk.Entry(reference_frame, width=40)
        self.ref_full_name_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        tk.Label(reference_frame, text="Address: ").grid(row=1, column=0, sticky="w")
        self.ref_address_entry = tk.Entry(reference_frame, width=40)
        self.ref_address_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        tk.Label(reference_frame, text="Phone Number: ").grid(row=2, column=0, sticky="w")
        self.ref_phone_entry = tk.Entry(reference_frame, width=40)
        self.ref_phone_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        tk.Label(reference_frame, text="Email Address: ").grid(row=3, column=0, sticky="w")
        self.ref_email_entry = tk.Entry(reference_frame, width=40)
        self.ref_email_entry.grid(row=3, column=1, padx=5, pady=5, sticky="w")

        tk.Label(reference_frame, text="LinkedIn Profile: ").grid(row=4, column=0, sticky="w")
        self.ref_linkedin_entry = tk.Entry(reference_frame, width=40)
        self.ref_linkedin_entry.grid(row=4, column=1, padx=5, pady=5, sticky="w")

        tk.Label(reference_frame, text="Website/Portfolio: ").grid(row=5, column=0, sticky="w")
        self.ref_website_entry = tk.Entry(reference_frame, width=40)
        self.ref_website_entry.grid(row=5, column=1, padx=5, pady=5, sticky="w")

        # Certification Frame
        certification_frame = tk.LabelFrame(main_frame, text="Certification", padx=10, pady=10)
        certification_frame.grid(row=2, column=1, padx=10, pady=10, sticky="nsw")

        # Treeview for displaying certification details
        self.cert_tree = ttk.Treeview(certification_frame, columns=("Name", "Link"), show='headings', height=5)
        self.cert_tree.heading("Name", text="Certification Name")
        self.cert_tree.heading("Link", text="Certification Link")
        self.cert_tree.grid(row=0, column=0, columnspan=3, padx=5, pady=5, sticky="nsew")

        # Buttons for adding, deleting, and editing certification details
        self.add_cert_btn = tk.Button(certification_frame, text="Add", command=self.add_certification)
        self.add_cert_btn.grid(row=1, column=0, padx=5, pady=5)

        self.edit_cert_btn = tk.Button(certification_frame, text="Edit", command=self.edit_certification)
        self.edit_cert_btn.grid(row=1, column=1, padx=5, pady=5)

        self.delete_cert_btn = tk.Button(certification_frame, text="Delete", command=self.delete_certification)
        self.delete_cert_btn.grid(row=1, column=2, padx=5, pady=5)

        #project frame
        project_frame = tk.LabelFrame(main_frame, text="Projects", padx=10, pady=10)
        project_frame.grid(row=2, column=2, padx=10, pady=10, sticky="nsw")

        # Treeview for displaying certification details
        self.proj_tree = ttk.Treeview(project_frame, columns=("Name", "Link"), show='headings', height=5)
        self.proj_tree.heading("Name", text="Prject Title")
        self.proj_tree.heading("Link", text="Github Link")
        self.proj_tree.grid(row=0, column=0, columnspan=3, padx=5, pady=5, sticky="nsew")

        # Buttons for adding, deleting, and editing certification details
        self.add_proj_btn = tk.Button(project_frame, text="Add", command=self.add_proj)
        self.add_proj_btn.grid(row=1, column=0, padx=5, pady=5)

        self.edit_proj_btn = tk.Button(project_frame, text="Edit", command=self.edit_proj)
        self.edit_proj_btn.grid(row=1, column=1, padx=5, pady=5)

        self.delete_proj_btn = tk.Button(project_frame, text="Delete", command=self.delete_proj)
        self.delete_proj_btn.grid(row=1, column=2, padx=5, pady=5)

        #button frame

        button_frame = tk.LabelFrame(main_frame, text="Commands", padx=10, pady=10)
        button_frame.grid(row=2, column=3, padx=10, pady=10, sticky="nsw")

        generate_btn = tk.Button(button_frame, text="Generate CV", command=self.generate_cv, bg="Black", fg="White")
        generate_btn.grid(row = 0, column = 0, padx = 15, pady = 10)

        clear_btn = tk.Button(button_frame, text="Clear Entries", command=self.clear_entries, bg="Black", fg="White")
        clear_btn.grid(row = 1, column = 0, padx = 15, pady = 10)

    def add_certification(self):
        self.cer_window = tk.Toplevel(self.root)
        self.cer_window.title("Add Certification")

        tk.Label(self.cer_window, text="Title:").grid(row=0, column=0, sticky="w")
        self.cer_entry = tk.Entry(self.cer_window, width=40)
        self.cer_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        tk.Label(self.cer_window, text="Link: ").grid(row=1, column=0, sticky="w")
        self.cur_link_entry = tk.Entry(self.cer_window, width=40)
        self.cur_link_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")


        tk.Button(self.cer_window, text="Save", command = self.save_cert).grid(row=5, column=0, columnspan=2, pady=10)

    def edit_certification(self):
        self.delete_certification()
        self.add_certification()

    def delete_certification(self):
        selected_item = self.cert_tree.selection()
        if selected_item:
            item_index = self.cert_tree.index(selected_item)
            self.cert_tree.delete(selected_item)
        else:
            messagebox.showwarning("Selection Error", "Please select an item to delete.")


    def save_cert(self):
        title = self.cer_entry.get()
        link = self.cur_link_entry.get()

        self.cert_tree.insert('', 'end', values=(title, link))
        self.cer_window.destroy()

    def generate_cv(self):
        filename = "generated_cv.pdf"
        document = SimpleDocTemplate(filename, pagesize=letter)
        styles = getSampleStyleSheet()

        elements = []

    # Adding Contact Information
        contact_info = [
            f"Full Name: {self.contact_full_name_entry.get()}",
            f"Address: {self.contact_address_entry.get()}",
            f"Phone Number: {self.contact_phone_entry.get()}",
            f"Email Address: {self.contact_email_entry.get()}",
            f"LinkedIn Profile: {self.contact_linkedin_entry.get()}",
            f"Website/Portfolio: {self.contact_website_entry.get()}"
        ]
        elements.append(Paragraph("Contact Information", styles['Heading2']))
        for info in contact_info:
            elements.append(Paragraph(info, styles['BodyText']))
        elements.append(Spacer(1, 12))

    # Adding Education Details
        elements.append(Paragraph("Education", styles['Heading2']))
        for child in self.education_tree.get_children():
            edu_values = self.education_tree.item(child, 'values')
            edu_info = f"{edu_values[0]}, {edu_values[1]}, {edu_values[2]}, Graduated: {edu_values[3]}, Honors: {edu_values[4]}"
            elements.append(Paragraph(edu_info, styles['BodyText']))
        elements.append(Spacer(1, 12))

        # Adding Work Experience
        elements.append(Paragraph("Work Experience", styles['Heading2']))
        for child in self.work_tree.get_children():
            work_values = self.work_tree.item(child, 'values')
            work_info = f"{work_values[0]} at {work_values[1]}, {work_values[2]}, {work_values[3]}"
            elements.append(Paragraph(work_info, styles['BodyText']))
            elements.append(Paragraph(work_values[4], styles['BodyText']))
            elements.append(Spacer(1, 6))
        elements.append(Spacer(1, 12))

    # Adding Skills
        elements.append(Paragraph("Skills", styles['Heading2']))
        elements.append(Paragraph(f"Technical Skills: {self.tech_skills_text.get('1.0', tk.END).strip()}", styles['BodyText']))
        elements.append(Paragraph(f"Soft Skills: {self.soft_skills_text.get('1.0', tk.END).strip()}", styles['BodyText']))
        elements.append(Paragraph(f"Languages: {self.languages_text.get('1.0', tk.END).strip()}", styles['BodyText']))
        elements.append(Spacer(1, 12))

    # Adding Certifications
        elements.append(Paragraph("Certifications", styles['Heading2']))
        for child in self.cert_tree.get_children():
            cert_values = self.cert_tree.item(child, 'values')
            cert_info = f"{cert_values[0]}: {cert_values[1]}"
            elements.append(Paragraph(cert_info, styles['BodyText']))
        elements.append(Spacer(1, 12))

    # Adding Projects
        elements.append(Paragraph("Projects", styles['Heading2']))
        for child in self.proj_tree.get_children():
            proj_values = self.proj_tree.item(child, 'values')
            proj_info = f"{proj_values[0]}: {proj_values[1]}"
            elements.append(Paragraph(proj_info, styles['BodyText']))
        elements.append(Spacer(1, 12))

    # Adding References
        elements.append(Paragraph("References", styles['Heading2']))
        ref_info = [
            f"Full Name: {self.ref_full_name_entry.get()}",
            f"Address: {self.ref_address_entry.get()}",
            f"Phone Number: {self.ref_phone_entry.get()}",
            f"Email Address: {self.ref_email_entry.get()}",
            f"LinkedIn Profile: {self.ref_linkedin_entry.get()}",
            f"Website/Portfolio: {self.ref_website_entry.get()}"
        ]
        for info in ref_info:
            elements.append(Paragraph(info, styles['BodyText']))
        elements.append(Spacer(1, 12))

    # Build the PDF document
        document.build(elements)
        messagebox.showinfo("CV Generated", f"Your CV has been generated and saved as {filename}")


    def add_proj(self):
        self.proj_window= tk.Toplevel(self.root)
        self.proj_window.title("Add Prject")

        tk.Label(self.proj_window, text="Title:").grid(row=0, column=0, sticky="w")
        self.proj_entry = tk.Entry(self.proj_window, width=40)
        self.proj_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        tk.Label(self.proj_window, text="Github Link: ").grid(row=1, column=0, sticky="w")
        self.link_entry = tk.Entry(self.proj_window, width=40)
        self.link_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")


        tk.Button(self.proj_window, text="Save", command = self.save_proj).grid(row=5, column=0, columnspan=2, pady=10)




    def edit_proj(self):
        self.delete_proj()
        self.add_proj()


    def delete_proj(self):
        selected_item = self.proj_tree.selection()
        if selected_item:
            item_index = self.proj_tree.index(selected_item)
            self.proj_tree.delete(selected_item)
        else:
            messagebox.showwarning("Selection Error", "Please select an item to delete.")


    def save_proj(self):
        title = self.proj_entry.get()
        link = self.link_entry.get()

        self.proj_tree.insert('', 'end', values=(title, link))
        self.proj_window.destroy()



    def add_education(self):
        self.edu_window = tk.Toplevel(self.root)
        self.edu_window.title("Add Education")

        tk.Label(self.edu_window, text="Institution Name:").grid(row=0, column=0, sticky="w")
        self.institution_entry = tk.Entry(self.edu_window, width=40)
        self.institution_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        tk.Label(self.edu_window, text="Degree:").grid(row=1, column=0, sticky="w")
        self.degree_entry = tk.Entry(self.edu_window, width=40)
        self.degree_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        tk.Label(self.edu_window, text="Field of Study:").grid(row=2, column=0, sticky="w")
        self.field_entry = tk.Entry(self.edu_window, width=40)
        self.field_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        tk.Label(self.edu_window, text="Graduation Date:").grid(row=3, column=0, sticky="w")
        self.graduation_date = DateEntry(self.edu_window, width=12, background='darkblue', foreground='white', borderwidth=2)
        self.graduation_date.grid(row=3, column=1, padx=5, pady=5, sticky="w")

        tk.Label(self.edu_window, text="Honors:").grid(row=4, column=0, sticky="w")
        self.honors_entry = tk.Entry(self.edu_window, width=40)
        self.honors_entry.grid(row=4, column=1, padx=5, pady=5, sticky="w")

        tk.Button(self.edu_window, text="Save", command=self.save_education).grid(row=5, column=0, columnspan=2, pady=10)

    def save_education(self):
        institution = self.institution_entry.get()
        degree = self.degree_entry.get()
        field = self.field_entry.get()
        graduation_date = self.graduation_date.get()
        honors = self.honors_entry.get()

        self.education_tree.insert('', 'end', values=(institution, degree, field, graduation_date, honors))
        self.edu_window.destroy()

    def delete_education(self):
        selected_item = self.education_tree.selection()[0]
        self.education_tree.delete(selected_item)

    def edit_education(self):
        selected_item = self.education_tree.selection()[0]
        values = self.education_tree.item(selected_item, 'values')

        self.edu_window = tk.Toplevel(self.root)
        self.edu_window.title("Edit Education")

        tk.Label(self.edu_window, text="Institution Name:").grid(row=0, column=0, sticky="w")
        self.institution_entry = tk.Entry(self.edu_window, width=40)
        self.institution_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        self.institution_entry.insert(0, values[0])

        tk.Label(self.edu_window, text="Degree:").grid(row=1, column=0, sticky="w")
        self.degree_entry = tk.Entry(self.edu_window, width=40)
        self.degree_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        self.degree_entry.insert(0, values[1])

        tk.Label(self.edu_window, text="Field of Study:").grid(row=2, column=0, sticky="w")
        self.field_entry = tk.Entry(self.edu_window, width=40)
        self.field_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")
        self.field_entry.insert(0, values[2])

        tk.Label(self.edu_window, text="Graduation Date:").grid(row=3, column=0, sticky="w")
        self.graduation_date = DateEntry(self.edu_window, width=12, background='darkblue', foreground='white', borderwidth=2)
        self.graduation_date.grid(row=3, column=1, padx=5, pady=5, sticky="w")
        self.graduation_date.set_date(values[3])

        tk.Label(self.edu_window, text="Honors:").grid(row=4, column=0, sticky="w")
        self.honors_entry = tk.Entry(self.edu_window, width=40)
        self.honors_entry.grid(row=4, column=1, padx=5, pady=5, sticky="w")
        self.honors_entry.insert(0, values[4])

        tk.Button(self.edu_window, text="Save", command=lambda: self.update_education(selected_item)).grid(row=5, column=0, columnspan=2, pady=10)

    def update_education(self, item):
        institution = self.institution_entry.get()
        degree = self.degree_entry.get()
        field = self.field_entry.get()
        graduation_date = self.graduation_date.get()
        honors = self.honors_entry.get()

        self.education_tree.item(item, values=(institution, degree, field, graduation_date, honors))
        self.edu_window.destroy()

    def add_work_experience(self):
        self.work_window = tk.Toplevel(self.root)
        self.work_window.title("Add Work Experience")

        tk.Label(self.work_window, text="Job Title:").grid(row=0, column=0, sticky="w")
        self.job_title_entry = tk.Entry(self.work_window, width=40)
        self.job_title_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        tk.Label(self.work_window, text="Company Name:").grid(row=1, column=0, sticky="w")
        self.company_entry = tk.Entry(self.work_window, width=40)
        self.company_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        tk.Label(self.work_window, text="Location:").grid(row=2, column=0, sticky="w")
        self.location_entry = tk.Entry(self.work_window, width=40)
        self.location_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        tk.Label(self.work_window, text="Dates of Employment:").grid(row=3, column=0, sticky="w")
        self.employment_dates_entry = DateEntry(self.work_window, width=12, background='darkblue', foreground='white', borderwidth=2)
        self.employment_dates_entry.grid(row=3, column=1, padx=5, pady=5, sticky="w")

        tk.Label(self.work_window, text="Responsibilities and Achievements:").grid(row=4, column=0, sticky="w")
        self.responsibilities_text = scrolledtext.ScrolledText(self.work_window, width=40, height=5, wrap=tk.WORD)
        self.responsibilities_text.grid(row=4, column=1, padx=5, pady=5, sticky="w")

        tk.Button(self.work_window, text="Save", command=self.save_work_experience).grid(row=5, column=0, columnspan=2, pady=10)


    def save_work_experience(self):
        job_title = self.job_title_entry.get()
        company = self.company_entry.get()
        location = self.location_entry.get()
        dates = self.employment_dates_entry.get()
        responsibilities = self.responsibilities_text.get("1.0", tk.END).strip()

        self.work_tree.insert('', 'end', values=(job_title, company, location, dates, responsibilities))
        self.work_window.destroy()

    def delete_work_experience(self):
        selected_item = self.work_tree.selection()[0]
        self.work_tree.delete(selected_item)

    def edit_work_experience(self):
        selected_item = self.work_tree.selection()[0]
        values = self.work_tree.item(selected_item, 'values')

        self.work_window = tk.Toplevel(self.root)
        self.work_window.title("Edit Work Experience")

        tk.Label(self.work_window, text="Job Title:").grid(row=0, column=0, sticky="w")
        self.job_title_entry = tk.Entry(self.work_window, width=40)
        self.job_title_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        self.job_title_entry.insert(0, values[0])

        tk.Label(self.work_window, text="Company Name:").grid(row=1, column=0, sticky="w")
        self.company_entry = tk.Entry(self.work_window, width=40)
        self.company_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        self.company_entry.insert(0, values[1])

        tk.Label(self.work_window, text="Location:").grid(row=2, column=0, sticky="w")
        self.location_entry = tk.Entry(self.work_window, width=40)
        self.location_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")
        self.location_entry.insert(0, values[2])

        tk.Label(self.work_window, text="Dates of Employment:").grid(row=3, column=0, sticky="w")
        self.employment_dates_entry = tk.Entry(self.work_window, width=40)
        self.employment_dates_entry.grid(row=3, column=1, padx=5, pady=5, sticky="w")
        self.employment_dates_entry.insert(0, values[3])

        tk.Label(self.work_window, text="Responsibilities and Achievements:").grid(row=4, column=0, sticky="w")
        self.responsibilities_text = scrolledtext.ScrolledText(self.work_window, width=40, height=5, wrap=tk.WORD)
        self.responsibilities_text.grid(row=4, column=1, padx=5, pady=5, sticky="w")
        self.responsibilities_text.insert(tk.END, values[4])

        tk.Button(self.work_window, text="Save", command=lambda: self.update_work_experience(selected_item)).grid(row=5, column=0, columnspan=2, pady=10)

    def update_work_experience(self, item):
        job_title = self.job_title_entry.get()
        company = self.company_entry.get()
        location = self.location_entry.get()
        dates = self.employment_dates_entry.get()
        responsibilities = self.responsibilities_text.get("1.0", tk.END).strip()

        self.work_tree.item(item, values=(job_title, company, location, dates, responsibilities))
        self.work_window.destroy()

    def clear_entries(self):
    # Clear Contact Information
        self.contact_full_name_entry.delete(0, tk.END)
        self.contact_address_entry.delete(0, tk.END)
        self.contact_phone_entry.delete(0, tk.END)
        self.contact_email_entry.delete(0, tk.END)
        self.contact_linkedin_entry.delete(0, tk.END)
        self.contact_website_entry.delete(0, tk.END)

    # Clear Education
        for item in self.education_tree.get_children():
            self.education_tree.delete(item)

    # Clear Work Experience
        for item in self.work_tree.get_children():
            self.work_tree.delete(item)

    # Clear Skills
        self.tech_skills_text.delete("1.0", tk.END)
        self.soft_skills_text.delete("1.0", tk.END)
        self.languages_text.delete("1.0", tk.END)

    # Clear References
        self.ref_full_name_entry.delete(0, tk.END)
        self.ref_address_entry.delete(0, tk.END)
        self.ref_phone_entry.delete(0, tk.END)
        self.ref_email_entry.delete(0, tk.END)
        self.ref_linkedin_entry.delete(0, tk.END)
        self.ref_website_entry.delete(0, tk.END)

    # Clear Certifications
        for item in self.cert_tree.get_children():
            self.cert_tree.delete(item)

    # Clear Projects
        for item in self.proj_tree.get_children():
            self.proj_tree.delete(item)




def run_cv_maker():
    root = tk.Tk()
    app = CVGeneratorApp(root)
    root.mainloop()

run_cv_maker()
