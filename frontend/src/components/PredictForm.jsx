import { useState } from "react"
import { Button, Form, InputGroup } from "react-bootstrap"

export default function PredictForm({ getPredict, setPredict, setError }) {

    var [date, setDate] = useState("")

    async function callFunc(event) {
        await event.preventDefault()
        if (date) {
            setError("")
            return await getPredict(date)
        } else {
            setPredict("")
            setError("Write date")
        }
    }

    return (
        <>
            <Form formAction="POST" onSubmit={e => callFunc(e)}>
                <Form.Group className="mb-3">
                    <InputGroup className="mb-3">
                        <Form.Control
                            type="date"
                            onChange={e => setDate((prev) => e.target.value)}
                        />
                        <Button
                            variant="outline-secondary"
                            id="button-addon1"
                            type="submit"
                        >
                            get predict
                        </Button>
                    </InputGroup>
                </Form.Group>
            </Form>
        </>
    )
}