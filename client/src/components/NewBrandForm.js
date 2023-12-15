import React from "react";
import { useFormik } from "formik";
import * as yup from "yup";
import { NavLink, useHistory } from "react-router-dom";

function NewBrandForm({brandList, setBrandList}) {

    const history = useHistory();

    const formSchema = yup.object().shape({
        name: yup.string().required(),
        description: yup.string().required().min(5).max(100)
    });

    const formik = useFormik({
        initialValues: {
            name: "",
            description: "",
        },
        validationSchema: formSchema,
        onSubmit: (values) => {
            fetch("/brands", {
                method: "POST",
                headers: {
                    "Accept": "application/json",
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(values, null, 2)
            })
            .then(resp => resp.json())
            .then(data => {
                const newBrandList = [...brandList, data[0]];
                setBrandList(newBrandList);
                history.push("/brands");
            })
        }
    })

    return (
        <div>
            <h2>New Brand Form Here</h2>
            <form autoComplete="off" onSubmit={formik.handleSubmit}>
                <label>Brand Name:</label>
                <input name="name" type="text" value={formik.values.name} onChange={formik.handleChange} />
                <br />
                <label>Description:</label>
                <input name="description" type="text" value={formik.values.description} onChange={formik.handleChange} />
                <br />
                <button type="submit">Submit New Brand</button>
            </form>
            <br />
            <NavLink to="/brands" exact>
                <button>Cancel</button>
            </NavLink>
        </div>
    )
};

export default NewBrandForm;