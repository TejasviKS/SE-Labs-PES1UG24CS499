# Lab 1 - Requirements Engineering & UML Use-Case Modelling

**Course:** Software Engineering
**Problem Statement:** #11 - Healthcare & Telemedicine
**Title:** Telemedicine Slot Booking & Prescription Portal

## Objective

The goal of this lab was to take the given scenario and:
1. Elicit functional and non-functional requirements from it.
2. Write them up in a structured requirements table (like an SRS).
3. Identify the actors and use cases for the system.
4. Draw a UML use-case diagram with at least one `<<include>>` and one `<<extend>>` relationship.
5. Write out one detailed use-case flow (main scenario + alternate flow).

## Problem Context

A secure healthcare consultation portal that allows remote patients to view doctor specialties, book video consultation slots, receive encrypted tele-consultation room links, and download digitally signed prescriptions after the consultation.

## Files in this repo

| File | Description |
|---|---|
| `Requirements_Table.docx` | Requirements table with 5 FRs (FR-001 to FR-005) and 2 NFRs (NFR-001, NFR-002). Each row has Req ID, Type, Description, Priority, Acceptance Criteria, and Rationale. FR-001 and NFR-001 were given in the problem statement; the rest were written for this lab. |
| `usecase_diagram.pdf` | UML use-case diagram for the system. Shows the system boundary, all actors, all use cases, and the required `<<include>>`/`<<extend>>` relationships. |
| `UseCase_Flow.docx` | One-page use-case flow for "Book Consultation Slot" (UC-02), including preconditions, postconditions, main success scenario, and an alternate flow. |
| `README.md` | This file. |

## Actors

- **Patient** - primary actor, searches for doctors, books slots, joins video calls, downloads prescriptions.
- **Physician** - conducts the video consultation and authors/signs the prescription.
- **Notification System** - external system that sends booking/confirmation notifications.

## Use Cases

| ID | Use Case | Notes |
|---|---|---|
| UC-01 | Search Doctors by Specialty | Patient filters doctors before booking |
| UC-02 | Book Consultation Slot | Core booking use case |
| UC-03 | Conduct Video Consultation | Physician-side use case |
| UC-04 | Author & Sign Prescription | Produces the signed PDF (linked to FR-001) |
| UC-05 | Download Prescription | Patient downloads the signed PDF |
| UC-06 | Send Booking Notification | `<<include>>` by UC-02 (always happens after a booking) |
| UC-07 | Reschedule Slot | `<<extend>>` UC-02 (only happens if patient chooses to reschedule) |

## Requirement Traceability (quick reference)

- FR-001 -> UC-04 (Author & Sign Prescription)
- FR-002 -> UC-01 (Search Doctors by Specialty)
- FR-003 -> UC-02 (Book Consultation Slot)
- FR-004 -> UC-03 (Conduct Video Consultation)
- FR-005 -> UC-05 (Download Prescription)
- NFR-001 -> applies across UC-03, UC-04, UC-05 (encryption of video/clinical data)
- NFR-002 -> applies to UC-03 (video consultation performance under load)

## How to view

- Open the `.docx` files in Microsoft Word or Google Docs.
- Open `usecase_diagram.pdf` in any PDF viewer.